# from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework import viewsets, mixins
from rest_framework.generics import CreateAPIView, DestroyAPIView

from api.serializers import SupportSerializer
from api.models import Support
from api.permissions import GetSupportPermission


class SupportViewSet(viewsets.GenericViewSet):
    """Description: SupportViewSet.

    API endpoint that allows support to be viewed, created, deleted or edited.
    """
    queryset = Support.objects.all()
    serializer_class = SupportSerializer
    permission_classes = (GetSupportPermission, )

    def destroy(self, request, pk=None):
        """
        API endpoint that allows one support to be deleted by user.
        """
        response = super(SupportViewSet, self).destroy(request, pk)
        return response
    
    @list_route(
        permission_classes=[GetSupportPermission],
        methods=['GET'],
        url_path='to_student' 
    )
    def get_support_made_to_student(self,request,id=None):
        """
        API endpoint that allows one student see all supports that have been made to him.
        ---
        Response example:
        ```
        {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
                {
                    "id": 7,
                    "message": "Yes you can",
                    "created_at": "2018-07-04T15:39:25.316130-03:00",
                    "student_from": 8,
                    "student_to": 8
                },
                {
                    "id": 6,
                    "message": "Teste 1",
                    "created_at": "2018-07-04T15:39:12.854664-03:00",
                    "student_from": 8,
                    "student_to": 8
                }
            ]
        }
        ```
        """
        supports = Support.objects.filter(student_to=request.user).order_by('-created_at')
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
        permission_classes=[GetSupportPermission],
        methods=['GET'],
        url_path='from_student' 
    )
    def get_support_made_from_student(self,request,id=None):
        """
        API endpoint that allows one student see all supports that he made.
        ---
        Response example:
        ```
        {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
                {
                    "id": 7,
                    "message": "Yes you can",
                    "created_at": "2018-07-04T15:39:25.316130-03:00",
                    "student_from": 8,
                    "student_to": 8
                },
                {
                    "id": 6,
                    "message": "Teste 1",
                    "created_at": "2018-07-04T15:39:12.854664-03:00",
                    "student_from": 8,
                    "student_to": 8
                }
            ]
        }
        ```
        """
        supports = Support.objects.filter(student_from=request.user).order_by('-created_at')
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


class SupportCreate(CreateAPIView, DestroyAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer
    permission_classes = (GetSupportPermission, )