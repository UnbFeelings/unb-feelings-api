from rest_framework.viewsets import ModelViewSet

from api.serializers import CourseSerializer
from api.models import Course
from api.permissions import NonAdminCanOnlyGet


class CourseViewSet(ModelViewSet):
    """Description: CourseViewSet.

    API endpoint that allows courses to be viewed, created, deleted or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (NonAdminCanOnlyGet, )

    def list(self, request):
        """
        API endpoint that allows all courses to be viewed.
        ---
        Response example:
        ```
        {
            "count": 6,
            "next": null,
            "previous": null,
            "results": [
            {
                "id": 1,
                "name": "ENGENHARIA",
                "campus": 1
            },
            {
                "id": 2,
                "name": "SOFTWARE",
                "campus": 1
            },
            {
                "id": 3,
                "name": "ELETRONICA",
                "campus": 1
            },
            {
                "id": 4,
                "name": "AEROESPACIAL",
                "campus": 1
            },
            {
                "id": 5,
                "name": "ENERGIA",
                "campus": 1
            },
            {
                "id": 6,
                "name": "AUTOMOTIVA",
                "campus": 1
            }
            ]
        }
        ```
        """
        return super(CourseViewSet, self).list(request)

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
        return super(CourseViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        API endpoint that allows courses to be deleted.
        """
        response = super(CourseViewSet, self).destroy(request, pk)
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
        response = super(CourseViewSet, self).retrieve(request, pk)
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
            super(CourseViewSet, self).partial_update(request, pk, **kwargs)
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
            super(CourseViewSet, self).update(request, pk, **kwargs)
        return response
