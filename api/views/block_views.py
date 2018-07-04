from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api.permissions import BlockPermissions
from api.serializers import BlockSerializer
from api.models import Block

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
        return Block.objects.filter(blocker=self.request.user)

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
        instance = Block.objects.get(blocked=pk, blocker=self.request.user)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
