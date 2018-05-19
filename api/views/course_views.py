from rest_framework.viewsets import ModelViewSet

from api.serializers import CourseSerializer
from api.models import Course


class CourseViewSet(ModelViewSet):
    """Description: CourseViewSet.

    API endpoint that allows courses to be viewed, created, deleted or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

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
                "name": "ENGENHARIA"
            },
            {
                "id": 2,
                "name": "SOFTWARE"
            },
            {
                "id": 3,
                "name": "ELETRONICA"
            },
            {
                "id": 4,
                "name": "AEROESPACIAL"
            },
            {
                "id": 5,
                "name": "ENERGIA"
            },
            {
                "id": 6,
                "name": "AUTOMOTIVA"
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
            "name": "MECATRONICA"
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
        "name": "MECATRONICA"
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
            "name": "CIVIL"
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
            "name": "CIVIL"
        }
        ```
        """
        response = \
            super(CourseViewSet, self).update(request, pk, **kwargs)
        return response
