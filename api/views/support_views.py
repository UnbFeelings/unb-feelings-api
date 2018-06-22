# from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework import viewsets, mixins

from api.serializers import SupportSerializer
from api.models import Support
from api.permissions import PostPermission


class SupportViewSet(mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet,
                    mixins.CreateModelMixin):
    """Description: SupportViewSet.

    API endpoint that allows support to be viewed, created, deleted or edited.
    """
    queryset = Support.objects.all()
    serializer_class = SupportSerializer
    permission_classes = (PostPermission, )
    
    @list_route(
        permission_classes=[],
        methods=['GET'],
        url_path='to_student/(?P<id>\d+)' 
    )
    def get_support_made_to_student(self,request,id=None):
        supports = Support.objects.filter(student_to=id)
        supports_paginated = self.paginate_queryset(supports)

        if supports_paginated is not None:
            serializer = SupportSerializer(
                data=supports_paginated, many=True, context={'request': request})

            serializer.is_valid()
            return self.get_paginated_response(serializer.data)
        else:

            data = SupportSerializer(
                data=supports, many=True, context={'request': request})

            data.is_valid()
            return Response(data.data)


    @list_route(
        permission_classes=[],
        methods=['GET'],
        url_path='from_student/(?P<id>\d+)' 
    )
    def get_support_made_from_student(self,request,id=None):
        supports = Support.objects.filter(student_from=id)
        supports_paginated = self.paginate_queryset(supports)

        if supports_paginated is not None:
            serializer = SupportSerializer(
                data=supports_paginated, many=True, context={'request': request})

            serializer.is_valid()
            return self.get_paginated_response(serializer.data)
        else:

            data = SupportSerializer(
                data=supports, many=True, context={'request': request})

            data.is_valid()
            return Response(data.data)



    def create(self, request):
        """
        API endpoint that allows all courses to be created.
        ---
        Body example:
        ```
        {
            "name": "MECATRONICA",
        }
        ```
        Response example:
        ```
        {
            "id": 7,
            "name": "MECATRONICA",
            "campus": 2
        }
        ```
        """
        return super(SupportViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        API endpoint that allows courses to be deleted.
        """
        response = super(SupportViewSet, self).destroy(request, pk)
        return response

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows a specific course to be viewed.
        ---
        Response example:
        ```
        {
        "id": 7,
        "name": "MECATRONICA",
        "campus": 2
        }
        ```
        """
        response = super(SupportViewSet, self).retrieve(request, pk)
        return response

