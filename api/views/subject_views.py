from rest_framework.viewsets import ModelViewSet

from api.serializers import SubjectSerializer
from api.models import Subject


class SubjectViewSet(ModelViewSet):
    """Description: StudentViewSet.

    API endpoint that allows subjects to be viewed, created, deleted or edited.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def list(self, request):
        """
        API endpoint that allows all subjects to be viewed.
        ---
        Response example:
        ```
        {
        "count": 3,
        "next": "http://localhost:8000/api/subjects/?limit=100&offset=100",
        "previous": null,
        "results": [
            {
                "id": 1,
                "name": "CÁLCULO 1                     ",
                "course": 1
            },
            {
                "id": 2,
                "name": "CÁLCULO 2                     ",
                "course": 1
            },
            {
                "id": 3,
                "name": "CÁLCULO 3                     ",
                "course": 1
            },
        }
        ```
        """
        response = super(SubjectViewSet, self).list(request)
        return response

    def create(self, request):
        """
        API endpoint that allows subjects to be created.
        ---
        Body example:
        ```
        {
          "name": "CALCULO 4",
          "course": 2
        }
        ```
        Response example:
        ```
        {
          "id": 4,
          "name": "CALCULO 4",
          "course": 2
        }
        ```
        """
        response = super(SubjectViewSet, self).create(request)
        return response

    def destroy(self, request, pk=None):
        """
        API endpoint that allows subjects to be deleted.
        """
        response = super(SubjectViewSet, self).destroy(request, pk)
        return response

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows a specific subject to be viewed.
        ---
        Response example:
        ```
          {
              "id": 1,
              "name": "CÁLCULO 1                     ",
              "course": 1
          }
        ```
        """
        response = super(SubjectViewSet, self).retrieve(request, pk)
        return response

    def partial_update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a subject to be partial edited.
        ---
        Body example:
        ```
        {
            "name": "CÁLCULO 5",
        }
        ```
        Response example:
        ```
        {
            "id": 1,
            "name": "CÁLCULO 5",
            "course": 1
        }
        ```
        """
        response = \
            super(SubjectViewSet, self).partial_update(request, pk, **kwargs)
        return response

    def update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a subject to be edited.
        ---
        Body example:
        ```
        {
            "name": "CÁLCULO 6",
            "course": 2
        }
        ```
        Response example:
        ```
        {
            "id": 1,
            "name": "CÁLCULO 6",
            "course": 2
        }
        ```
        """
        response = super(SubjectViewSet, self).update(request, pk, **kwargs)
        return response
