from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import (
    Course, Post, Student, Subject, Tag
)
from .permissions import (
    AdminItemPermissions, StudentPermissions
)
from .serializers import (
    CourseSerializer, PostSerializer, StudentSerializer, SubjectSerializer,
    TagSerializer
)


class CourseViewSet(ModelViewSet):
    permission_classes = (AdminItemPermissions,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SubjectViewSet(ModelViewSet):
    permission_classes = (AdminItemPermissions,)
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class StudentViewSet(ModelViewSet):
    """Description: StudentViewSet.

    API endpoint that allows users to be viewed, created, deleted or edited.
    """
    permission_classes = (StudentPermissions,)
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
        for student in response.data['results']:
            course = Course.objects.get(id=student['course'])
            course_serializer = CourseSerializer(course)
            student['course'] = course_serializer.data
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
        course = Course.objects.get(id=response.data['course'])
        course_serializer = CourseSerializer(course)
        response.data['course'] = course_serializer.data
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
        course = Course.objects.get(id=response.data['course'])
        course_serializer = CourseSerializer(course)
        response.data['course'] = course_serializer.data
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
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
