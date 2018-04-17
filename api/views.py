from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from rest_framework_jwt.views import ObtainJSONWebToken

from .models import (
    Campus, Course, Post, Student, Subject, Tag, Emotion
)
from .permissions import (
    AdminItemPermissions, StudentPermissions
)
from .serializers import (
    CampusSerializer, CourseSerializer, PostSerializer, StudentSerializer,
    SubjectSerializer, TagSerializer, EmotionSerializer
)


class CampusViewSet(ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer


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
            "name": "CÁLCULO 5",
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
            "name": "CÁLCULO 6",
            "course": 2
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

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class StudentViewSet(ModelViewSet):
    """Description: StudentViewSet.

    API endpoint that allows users to be viewed, created, deleted or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (StudentPermissions,)

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
    """Description: TagViewSet.

    API endpoint that allows tags to be viewed, created, deleted or edited.
    """

    def list(self, request):
      """
      API endpoint that allows all tags to be viewed.
      ---
      Response example:
      ```
      {
          "count": 1,
          "next": null,Tag
          "previous": null,
          "results": [
              {
                  "id": 1,
                  "description": "TAG1",
                  "quantity": 1
              }
          ]
      }
      ```
      """
      response = super(TagViewSet, self).list(request)
      return response

    def create(self, request):
        """
        API endpoint that allows tags to be created.
        ---
        Body example:
        ```
        {
          "description": "educacao",
        }
        ```
        Response example:
        ```
        {
            "id": 2,
            "description": "educacao",
            "quantity": 0
        }
        ```
        """
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            instance, created = serializer.get_or_create()
            if not created:
                serializer.update(instance, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        API endpoint that allows tags to be deleted.
        """
        response = super(TagViewSet, self).destroy(request, pk)
        return response

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows a specific tag to be viewed.
        ---
        Response example:
        ```
        {
            "id": 1,
            "description": "TAG1",
            "quantity": 1
        }
        ```
        """
        response = super(TagViewSet, self).retrieve(request, pk)
        return response

    def partial_update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a tag to be partial edited.
        ---
        Body example:
        ```
        {
            "id": 1,
            "description": "TAG1",
            "quantity": 1
        }
        ```
        Response example:
        ```
        {
            "id": 1,
            "description": "TAG1",
            "quantity": 2
        }
        ```
        """
        response = \
            super(TagViewSet, self).partial_update(request, pk, **kwargs)
        return response

    def update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a tag to be edited.
        ---
        Body example:
        ```
        {
            "description": "TAG2",
            "quantity": 2
        }
        ```
        Response example:
        ```
        {
            "id": 1,
            "description": "TAG2",
            "quantity": 2
        }
        ```
        """
        response = super(TagViewSet, self).update(request, pk, **kwargs)
        return response


    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostViewSet(ModelViewSet):
    """Description: PostViewSet.

    API endpoint that allows posts to be viewed, created, deleted or edited.
    """

    def list(self, request):
      """
      API endpoint that allows all posts to be viewed.
      ---
      Response example:
      ```
      {
          "count": 1,
          "next": null,
          "previous": null,
          "results": [
              {
                  "id": 1,
                  "author": 1,
                  "content": "asdfasd",
                  "subject": 15,
                  "tag": [
                      1
                  ]
              }
          ]
      }
      ```
      """
      response = super(PostViewSet, self).list(request)
      return response

    def create(self, request):
        """
        API endpoint that allows posts to be created.
        ---
        Body example:
        ```
        {
            "author": pedro_1195@hotmail.com,
            "content": "Quero morrer",
            "subject": COMBUSTIVEIS E BIOCOMBUSTIVEIS,
            "tag": [
                TAG1,
                educacao
            ]
        }
        ```
        Response example:
        ```
        {
            "id": 2,
            "author": 1,
            "content": "Quero morrer",
            "subject": 11,
            "tag": [
                1,
                2
            ]
        }
        ```
        """
        response = super(PostViewSet, self).create(request)
        return response

    def destroy(self, request, pk=None):
        """
        API endpoint that allows posts to be deleted.
        """
        response = super(PostViewSet, self).destroy(request, pk)
        return response

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows a specific post to be viewed.
        ---
        Response example:
        ```
        {
            "id": 1,
            "author": 1,
            "content": "asdfasd",
            "subject": 15,
            "tag": [
                1
            ]
        }
        ```
        """
        response = super(PostViewSet, self).retrieve(request, pk)
        return response

    def partial_update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a post to be partial edited.
        ---
        Body example:
        ```
        {
            "content": "Melhor aula do mundo",
        }
        ```
        Response example:
        ```
        {
        {
            "id": 1,
            "author": 1,
            "content": "Melhor aula do mundo",
            "subject": 15,
            "tag": [
                1
            ]
        }
        }
        ```
        """
        response = \
            super(PostViewSet, self).partial_update(request, pk, **kwargs)
        return response

    def update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a post to be edited.
        ---
        Body example:
        ```
        {
          {
              "author": hpedro1195@gmail.com,
              "content": "Pior aula do mundo",
              "subject": 15,
              "tag": [
                TAG1,
                educacao
              ]
          }
        }
        ```
        Response example:
        ```
        {
          {
              "id": 1,
              "author": hpedro1195@gmail.com,
              "content": "Pior aula do mundo",
              "subject": 15,
              "tag": [
                1,
                2
              ]
          }
        }
        ```
        """
        response = super(PostViewSet, self).update(request, pk, **kwargs)
        return response

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EmotionViewSet(ModelViewSet):
    """Description: EmotionViewSet.

    API endpoint that allows emotions to be viewed, created, deleted or edited.
    """
    def list(self, request):
      """
      API endpoint that allows all courses to be viewed.
      ---
      Response example:
      ```
      {
        "count": 4,
        "next": null,
        "previous": null,
        "results": [
          {
            "id": 1,
            "name": "Miserável"
          },
          {
            "id": 2,
            "name": "Infeliz"
          },
          {
            "id": 3,
            "name": "Triste"
          },
          {
            "id": 4,
            "name": "Amargurado"
          }
        ]
      }
      ```
      """
      return super(EmotionViewSet, self).list(request)

    def create(self, request):
      """
      API endpoint that allows all emotions to be created.
      ---
      Body example:
      ```
      {
        "name": "Deprimido",
      }
      ```
      Response example:
      ```
      {
        "id": 1,
        "name": "Deprimido"
      }
      ```
      """
      return super(EmotionViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        API endpoint that allows emotions to be deleted.
        """
        response = super(EmotionViewSet, self).destroy(request, pk)
        return response

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows a specific emotions to be viewed.
        ---
        Response example:
        ```
        {
          "id": 7,
          "name": "Depressivo"
        }
        ```
        """
        response = super(EmotionViewSet, self).retrieve(request, pk)
        return response

    def partial_update(self, request, pk=None, **kwargs):
      """
      API endpoint that allows a emotions to be partial edited.
      ---
      Body example:
      ```
      {
        "name": "Abalado"
      }
      ```
      Response example:
      ```
      {
        "id": 7,
        "name": "Abalado"
      }
      ```
      """
      response = \
          super(EmotionViewSet, self).partial_update(request, pk, **kwargs)
      return response

    def update(self, request, pk=None, **kwargs):
      """
      API endpoint that allows a emotions to be edited.
      ---
      Body example:
      ```
      {
        "name": "Desanimado"
      }
      ```
      Response example:
      ```
      {
        "id": 7,
        "name": "Desanimado"
      }
      ```
      """
      response = \
          super(EmotionViewSet, self).update(request, pk, **kwargs)
      return response
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer


class CustomObtainJWTToken(ObtainJSONWebToken):

    def post(self, request, *args, **kwargs):
        response = \
            super(CustomObtainJWTToken, self).post(request, *args, **kwargs)

        user = Student.objects.get(email=request.data['email'])
        response.data['user'] = user.pk

        return response
