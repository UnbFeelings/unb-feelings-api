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
            if (self.request.method == 'POST' and
                    self.request.user.is_anonymous):
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
