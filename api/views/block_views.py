from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.permissions import BlockPermissions
from api.serializers import BlockSerializer

class BlockViewSet(ModelViewSet):
    """Description: BlockViewSet.

    API endpoint that allows blocks to be listed, created or deleted.
    """
    permission_classes = (BlockPermissions, )
    serializer_class = BlockSerializer

    def get_queryset(self):
        """
        Override of query set method to return only user blocked users
        """
        return self.request.user.list_blocked_users()

    def list(self, request):
        """
        API endpoint that allows user to list all their blocks.
        """
        response = super(BlockViewSet, self).list(request)
        return response

    def create(self, request):
        """
        API endpoint that allows user to block other user
        """
        response = super(BlockViewSet, self).create(request)

        return response

    def destroy(self, request, pk=None):
        """
        API endpoint that allows blocks to be deleted.
        """
        response = super(StudentViewSet, self).destroy(request, pk)
        return response
