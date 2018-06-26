from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.permissions import BlockPermissions

class BlockViewSet(ModelViewSet):
    """Description: BlockViewSet.

    API endpoint that allows blocks to be listed, created or deleted.
    """
    permission_classes = (BlockPermissions, )

    def list(self, request):
        """
        API endpoint that allows user to list all their blocks.
        """
        blocked_users = request.user.list_blocked_users()
        return None

    def create(self, request, blocked_id):
        """
        API endpoint that allows user to block other user
        """
        request.user.block_user(user_id)
        return None

    def destroy(self, request, pk=None):
        """
        API endpoint that allows blocks to be deleted.
        """
        response = super(StudentViewSet, self).destroy(request, pk)
        return response
