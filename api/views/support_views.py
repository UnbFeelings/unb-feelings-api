from rest_framework.viewsets import ModelViewSet

from api.serializers import SupportSerializer
from api.models import Support
from api.permissions import PostPermission


class SupportViewSet(ModelViewSet):
    """Description: SupportViewSet.

    API endpoint that allows support to be viewed, created, deleted or edited.
    """
    queryset = Support.objects.all()
    serializer_class = SupportSerializer
    permission_classes = (PostPermission, )

    def list(self, request):
        """
        API endpoint that allows all supports to be viewed.
        ---
        Response example:
        ```

        ```
        """
        return super(SupportViewSet, self).list(request)

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

    def partial_update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a course to be partial edited.
        ---
        Body example:
        ```
        {
            "name": "CIVIL"
        }
        ```
        Response example:
        ```
        {
            "id": 7,
            "name": "CIVIL",
            "campus": 2
        }
        ```
        """
        response = \
            super(SupportViewSet, self).partial_update(request, pk, **kwargs)
        return response

    def update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a course to be edited.
        ---
        Body example:
        ```
        {
            "name": "CIVIL"
        }
        ```
        Response example:
        ```
        {
            "id": 7,
            "name": "CIVIL",
            "campus": 2
        }
        ```
        """
        response = \
            super(SupportViewSet, self).update(request, pk, **kwargs)
        return response
