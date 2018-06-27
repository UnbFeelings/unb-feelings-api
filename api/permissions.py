from django.core.exceptions import ObjectDoesNotExist

from rest_framework import permissions


class DefaultPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        permission = super().has_permission(request, view)

        try:
            if permission and request.user.is_active:
                permission = True
        except ObjectDoesNotExist:
            permission = False

        return permission


class StudentPermissions(permissions.BasePermission):
    def __init__(self):
        self.permission = False
        self.request = None
        self.user_id = ''
        self.user_request_id = ''
        self.authorized_user = False

    def has_permission(self, request, view):

        if request.user.is_superuser:
            return True

        elif 'users' in request.path:
            self.request = request
            self.user_id = str(self.request.user.id)
            self.user_request_id = \
                self.request.path.split('/users/')[1][:-1]
            if (self.request.method == 'POST'
                    and self.request.user.is_anonymous):
                self.permission = True

            if self.user_id == self.user_request_id:
                self.authorized_user = True

            if self.request.method != 'DELETE' and self.authorized_user:
                self.permission = True
        else:
            self.permission = True

        return self.permission


class AdminItemPermissions(permissions.BasePermission):
    def __init__(self):
        self.permission = False

    def has_permission(self, request, view):

        if 'courses' in request.path or 'subjects' in request.path:
            if request.method == 'GET':
                self.permission = True
            elif request.method != 'GET' and request.user.is_superuser:
                self.permission = True

        else:
            self.permission = True

        return self.permission


class NonAdminCanOnlyGet(permissions.BasePermission):
    """
    Non admin members can only use get requests
    """

    def has_permission(self, request, view):
        return self._base_check(request)

    def has_object_permission(self, request, view, obj):
        return self._base_check(request)

    def _base_check(self, request):
        if request.method == "GET":
            return True
        else:
            return request.user and request.user.is_staff


class PostPermission(permissions.BasePermission):
    """
    Admins and the post owner can do all requests.
    But others users(even anon users) only do GET requests
    """

    def has_permission(self, request, view):
        """
        Permissions for routes:
            GET /posts/
            POST /posts/
        """
        if request.method == "GET":
            return True

        if not request.user:
            return False

        return request.user.is_authenticated

    def has_object_permission(self, request, view, post):
        """
        Permissions for routes:
            GET /posts/:id
            PUT/PATCH /posts/:id
            DELETE /posts/:id
        """
        if request.method == "GET":
            return True

        if not request.user:
            return False

        if request.user.is_staff:
            return True

        return post.author == request.user

class BlockPermissions(permissions.BasePermission):
    """
    Only logged users can access block class view set
    """

    def has_permission(self, request, view):
        """
        Permissions for routes:
            GET /posts/
            POST /posts/
        """
        if not request.user:
            return False

        if request.user.is_anonymous:
            return False

        return request.user.is_authenticated

    def has_object_permission(self, request, view, block):
        """
        Permissions for routes:
            GET /posts/:id
            PUT/PATCH /posts/:id
            DELETE /posts/:id
        """

        if not request.user:
            return False

        return block.blocker == request.user
