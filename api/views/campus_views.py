from rest_framework.viewsets import ModelViewSet

from api.serializers import CampusSerializer
from api.models import Campus
from api.permissions import NonAdminCanOnlyGet


class CampusViewSet(ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
    permission_classes = (NonAdminCanOnlyGet, )

    def list(self, request):
        return super(CampusViewSet, self).list(request)
