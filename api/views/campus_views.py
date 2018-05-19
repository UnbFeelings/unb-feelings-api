from rest_framework.viewsets import ModelViewSet

from api.serializers import CampusSerializer
from api.models import Campus


class CampusViewSet(ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
