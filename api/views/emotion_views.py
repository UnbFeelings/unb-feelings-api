from rest_framework.viewsets import ModelViewSet

from api.serializers import EmotionSerializer
from api.models import Emotion


class EmotionViewSet(ModelViewSet):
    """Description: EmotionViewSet.

    API endpoint that allows emotions to be viewed, created, deleted or edited.
    """
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer

    def list(self, request):
        """
        API endpoint that allows all courses to be viewed.
        ---
        Response example:
        ```
        {
        "count": 4,
        "next": null,
        "previous": null,
        "results": [
            {
            "id": 1,
            "name": "Miserável"
            },
            {
            "id": 2,
            "name": "Infeliz"
            },
            {
            "id": 3,
            "name": "Triste"
            },
            {
            "id": 4,
            "name": "Amargurado"
            }
        ]
        }
        ```
        """
        return super(EmotionViewSet, self).list(request)

    def create(self, request):
        """
        API endpoint that allows all emotions to be created.
        ---
        Body example:
        ```
        {
        "name": "Deprimido",
        }
        ```
        Response example:
        ```
        {
        "id": 1,
        "name": "Deprimido"
        }
        ```
        """
        return super(EmotionViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        API endpoint that allows emotions to be deleted.
        """
        response = super(EmotionViewSet, self).destroy(request, pk)
        return response

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows a specific emotions to be viewed.
        ---
        Response example:
        ```
        {
            "id": 7,
            "name": "Depressivo"
        }
        ```
        """
        response = super(EmotionViewSet, self).retrieve(request, pk)
        return response

    def partial_update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a emotions to be partial edited.
        ---
        Body example:
        ```
        {
        "name": "Abalado"
        }
        ```
        Response example:
        ```
        {
        "id": 7,
        "name": "Abalado"
        }
        ```
        """
        response = \
            super(EmotionViewSet, self).partial_update(request, pk, **kwargs)
        return response

    def update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a emotions to be edited.
        ---
        Body example:
        ```
        {
        "name": "Desanimado"
        }
        ```
        Response example:
        ```
        {
        "id": 7,
        "name": "Desanimado"
        }
        ```
        """
        response = \
            super(EmotionViewSet, self).update(request, pk, **kwargs)
        return response
