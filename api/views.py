from rest_framework.viewsets import ModelViewSet

from .models import (
    Course, Post, Student, Subject, Tag
)
from .serializers import (
    CourseSerializer, PostSerializer, StudentSerializer, SubjectSerializer,
    TagSerializer
)


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class StudentViewSet(ModelViewSet):
    """Description: StudentViewSet.

    API endpoint that allows users to be viewed, created, deleted or edited.
    """
    # permission_classes = (StudentPermissions,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request):
        """
        API endpoint that allows all users to be viewed.
        ---
        Response example:
        Return a list of:
        ```
        {
            "id": "integer",
            "email": "string@email.com"
        }
        ```
        """
        response = super(StudentViewSet, self).list(request)
        return response

    def create(self, request):
        """
        API endpoint that allows users to be created.
        ---
        Body example:
        ```
        {
            "email": "string@email.com",
            "password": "string"
        }
        ```
        Response example:
        ```
        {
            "id": 1,
            "email": "string@email.com"
        }
        ```
        """
        response = super(StudentViewSet, self).create(request)
        return response

    def destroy(self, request, pk=None):
        """
        API endpoint that allows users to be deleted.
        """
        response = super(StudentViewSet, self).destroy(request, pk)
        return response

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows allow the return\
        of a user through the method Get.
        ---
        Response example:
        ```
        {
            "id": "integer",
            "email": "string@email.com"
        }
        ```
        """
        response = super(StudentViewSet, self).retrieve(request, pk)
        return response

    def partial_update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a user to be partial edited.
        ---
        Parameters:
        User ID and a JSON with one or more attributes of user

        Example:
        ```
        {
            "email": "string@email.com"
        }
        ```
        """
        response = \
            super(StudentViewSet, self).partial_update(request, pk, **kwargs)
        return response

    def update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a user to be edited.
        ---
        Parameters:
        User ID and a JSON with at least username,
        telephone and password of user
        Example:
        ```
        {
            "username": "string",
            "password": "string"
        }
        ```
        """
        response = super(
            StudentViewSet,
            self).update(
            request,
            pk,
            **kwargs
            )
        return response


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
