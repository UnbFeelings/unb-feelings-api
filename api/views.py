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
    """Description: CourseViewSet.

    API endpoint that allows courses to be viewed, created, deleted or edited.
    """
    def list(self, request):
      """
      API endpoint that allows all courses to be viewed.
      ---
      Response example:
      ```
      {
        "count": 6,
        "next": null,
        "previous": null,
        "results": [
          {
            "id": 1,
            "name": "ENGENHARIA"
          },
          {
            "id": 2,
            "name": "SOFTWARE"
          },
          {
            "id": 3,
            "name": "ELETRONICA"
          },
          {
            "id": 4,
            "name": "AEROESPACIAL"
          },
          {
            "id": 5,
            "name": "ENERGIA"
          },
          {
            "id": 6,
            "name": "AUTOMOTIVA"
          }
        ]
      }
      ```
      """
      return super(CourseViewSet, self).list(request)
    
    def create(self, request):
      """
      API endpoint that allows all courses to be created.
      ---
      Body example:
      ```
      {
        "name": "MECATRONICA",
      }
      ```
      Response example:
      ```
      {
        "id": 7,
        "name": "MECATRONICA"
      }
      ```
      """
      return super(CourseViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        API endpoint that allows courses to be deleted.
        """
        response = super(CourseViewSet, self).destroy(request, pk)
        return response

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows a specific course to be viewed.
        ---
        Response example:
        ```
        {
          "id": 7,
          "name": "MECATRONICA"
        }
        ```
        """
        response = super(CourseViewSet, self).retrieve(request, pk)
        return response
    
    def partial_update(self, request, pk=None, **kwargs):
      """
      API endpoint that allows a course to be partial edited.
      ---
      Body example:
      ```
      {
        "name": "CIVIL"
      }
      ```
      Response example:
      ```
      {
        "id": 7,
        "name": "CIVIL"
      }
      ```
      """
      response = \
          super(CourseViewSet, self).partial_update(request, pk, **kwargs)
      return response

    def update(self, request, pk=None, **kwargs):
      """
      API endpoint that allows a course to be edited.
      ---
      Body example:
      ```
      {
        "name": "CIVIL"
      }
      ```
      Response example:
      ```
      {
        "id": 7,
        "name": "CIVIL"
      }
      ```
      """
      response = \
          super(CourseViewSet, self).update(request, pk, **kwargs)
      return response
    permission_classes = (AdminItemPermissions,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SubjectViewSet(ModelViewSet):
    """Description: StudentViewSet.

    API endpoint that allows subjects to be viewed, created, deleted or edited.
    """
    
    def list(self, request):
      """
      API endpoint that allows all subjects to be viewed.
      ---
      Response example:
      ```
      {
      "count": 3,
      "next": "http://localhost:8000/api/subjects/?limit=100&offset=100",
      "previous": null,
      "results": [
          {
              "id": 1,
              "name": "CÁLCULO 1                     ",
              "course": 1
          },
          {
              "id": 2,
              "name": "CÁLCULO 2                     ",
              "course": 1
          },
          {
              "id": 3,
              "name": "CÁLCULO 3                     ",
              "course": 1
          },
      }
      ```
      """
      response = super(SubjectViewSet, self).list(request)
      return response

    def create(self, request):
        """
        API endpoint that allows subjects to be created.
        ---
        Body example:
        ```
        {
          "name": "CALCULO 4",
          "course": 2
        }
        ```
        Response example:
        ```
        {
          "id": 4,
          "name": "CALCULO 4",
          "course": 2
        }
        ```
        """
        response = super(SubjectViewSet, self).create(request)
        return response
        
    def destroy(self, request, pk=None):
        """
        API endpoint that allows subjects to be deleted.
        """
        response = super(SubjectViewSet, self).destroy(request, pk)
        return response
    
    def retrieve(self, request, pk=None):
        """
        API endpoint that allows a specific subject to be viewed.
        ---
        Response example:
        ```
          {
              "id": 1,
              "name": "CÁLCULO 1                     ",
              "course": 1
          }
        ```
        """
        response = super(SubjectViewSet, self).retrieve(request, pk)
        return response

    def partial_update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a subject to be partial edited.
        ---
        Body example:
        ```
        {
            "id": 1,
            "name": "CÁLCULO 1",
            "course": 1
        }
        ```
        Response example:
        ```
        {
            "id": 1,
            "name": "CÁLCULO 5",
            "course": 1
        }
        ```
        """
        response = \
            super(SubjectViewSet, self).partial_update(request, pk, **kwargs)
        return response
    
    def update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a subject to be edited.
        ---
        Body example:
        ```
        {
            "id": 1,
            "name": "CÁLCULO 5",
            "course": 1
        }
        ```
        Response example:
        ```
        {
            "id": 1,
            "name": "CÁLCULO 6",
            "course": 2
        }
        ```
        """
        response = super(SubjectViewSet, self).update(request, pk, **kwargs)
        return response

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
        ```
        {
          "count": 2,
          "next": null,
          "previous": null,
          "results": [
            {
              "id": 1,
              "email": "johndoe_1@email.com",
              "course": {
                "id": 1,
                "name": "Engenharia de Software"
              }
            },
            {
              "id": 2,
              "email": "johndoe_2@email.com",
              "course": {
                "id": 3,
                "name": "Engenharia Eletrônica"
              }
            }
          ]
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
          "email": "johndoe@email.com",
          "password": "string123",
          "course": 1
        }
        ```
        Response example:
        ```
        {
          "id": 1,
          "email": "johndoe@email.com",
          "course": {
            "id": 1,
            "name": "Engenharia de Software"
          }
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
        API endpoint that allows a specific user to be viewed.
        ---
        Response example:
        ```
        {
          "id": 1,
          "email": "johndoe@email.com",
          "course": {
            "id": 1,
            "name": "Engenharia de Software"
          }
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
        Body example:
        ```
        {
          "email": "string@email.com"
        }
        ```
        Response example:
        ```
        {
          "id": 1,
          "email": "string@email.com",
          "course": {
            "id": 1,
            "name": "Engenharia de Software"
          }
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
        Body example:
        ```
        {
          "email": "string@email.com",
          "password": "string123",
          "course": 3
        }
        ```
        Response example:
        ```
        {
          "id": 1,
          "email": "string@email.com",
          "course": {
            "id": 3,
            "name": "Engenharia Eletrônica"
          }
        }
        ```
        """
        response = super(StudentViewSet, self).update(request, pk, **kwargs)
        course = Course.objects.get(id=response.data['course'])
        course_serializer = CourseSerializer(course)
        response.data['course'] = course_serializer.data
        return response


class TagViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostViewSet(ModelViewSet):
    """Description: CourseViewSet.

    API endpoint that allows courses to be viewed, created, deleted or edited.
    """

    #permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
