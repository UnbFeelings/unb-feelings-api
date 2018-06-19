from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from api.serializers import TagSerializer
from api.models import Tag


class TagViewSet(ModelViewSet):
    """Description: TagViewSet.

    API endpoint that allows tags to be viewed, created, deleted or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def list(self, request):
        """
        API endpoint that allows all tags to be viewed.
        ---
        Response example:
        ```
        {
            "count": 1,
            "next": null,Tag
            "previous": null,
            "results": [
                {
                    "id": 1,
                    "description": "TAG1",
                    "quantity": 1
                }
            ]
        }
        ```
        """
        response = super(TagViewSet, self).list(request)
        return response

    def create(self, request):
        """
        API endpoint that allows tags to be created.
        ---
        Body example:
        ```
        {
          "description": "educacao"
        }
        ```
        Response example:
        ```
        {
            "id": 2,
            "description": "educacao",
            "quantity": 0
        }
        ```
        """
        serializer = TagSerializer(data=request.data)

        tag_retrieved = -1
        try:
            # trying to find the object on database
            obj = Tag.objects.get(description=request.data['description'])
            tag_retrieved = obj
        except Tag.DoesNotExist:
            pass

        if serializer.is_valid():
            instance, created = serializer.get_or_create()
            if not created:
                serializer.update(instance, serializer.validated_data)
            tag_data = Tag.objects.get(description=request.data['description'])
            tag_data = {
                'id': tag_data.pk,
                'description': tag_data.description,
                'quantity': tag_data.quantity
            }
            return Response(tag_data, status=status.HTTP_202_ACCEPTED)

        if tag_retrieved != -1:
            # if tag exists, we need to pass its id
            tag_data = {
                'id': tag_retrieved.pk,
                'description': tag_retrieved.description,
                'quantity': tag_retrieved.quantity
            }
            return Response(tag_data, status=status.HTTP_202_ACCEPTED)
        else:
            # any error from validation will enter here
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        API endpoint that allows tags to be deleted.
        """
        response = super(TagViewSet, self).destroy(request, pk)
        return response

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows a specific tag to be viewed.
        ---
        Response example:
        ```
        {
            "id": 1,
            "description": "TAG1",
            "quantity": 1
        }
        ```
        """
        response = super(TagViewSet, self).retrieve(request, pk)
        return response

    def partial_update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a tag to be partial edited.
        ---
        Body example:
        ```
        {
            "id": 1,
            "description": "TAG1",
            "quantity": 1
        }
        ```
        Response example:
        ```
        {
            "id": 1,
            "description": "TAG1",
            "quantity": 2
        }
        ```
        """
        response = \
            super(TagViewSet, self).partial_update(request, pk, **kwargs)
        return response

    def update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a tag to be edited.
        ---
        Body example:
        ```
        {
            "description": "TAG2",
            "quantity": 2
        }
        ```
        Response example:
        ```
        {
            "id": 1,
            "description": "TAG2",
            "quantity": 2
        }
        ```
        """
        response = super(TagViewSet, self).update(request, pk, **kwargs)
        return response
