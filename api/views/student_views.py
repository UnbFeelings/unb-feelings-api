from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.serializers import StudentSerializer, CourseSerializer
from api.models import Student, Course
from api.permissions import StudentPermissions

import json
import random
import os.path
import time


class StudentViewSet(ModelViewSet):
    """Description: StudentViewSet.

    API endpoint that allows users to be viewed, created, deleted or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (StudentPermissions, )

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
                "name": "Engenharia de Software",
                "campus": 1
              }
            },
            {
              "id": 2,
              "email": "johndoe_2@email.com",
              "course": {
                "id": 3,
                "name": "Engenharia Eletrônica",
                "campus": 1
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
            "name": "Engenharia de Software",
            "campus": 1
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
            "name": "Engenharia de Software",
            "campus": 1
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
            "name": "Engenharia de Software",
            "campus": 1
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
            "name": "Engenharia Eletrônica",
            "campus": 1
          }
        }
        ```
        """
        response = super(StudentViewSet, self).update(request, pk, **kwargs)
        course = Course.objects.get(id=response.data['course'])
        course_serializer = CourseSerializer(course)
        response.data['course'] = course_serializer.data
        return response

    @api_view(['GET'])
    def anonymous_name(request):
        """
        API endpoint that allows getting an anonymous name to a student.
        ---
        Response example:
        ```
        {
            "anonymous_name": "Rio"
        }
        ```
        """
        # The city names are sorted in alphabetic order
        last_modification_time = int(os.path.getmtime('api/fixtures/city_names.json'))
        current_time = int(time.time())

        CITY_NAMES = json.loads(open("api/fixtures/city_names.json").read())
        if(current_time - last_modification_time > 2):
            random.shuffle(CITY_NAMES)
            with open('api/fixtures/city_names.json', 'w') as the_file:
                        the_file.write(json.dumps(CITY_NAMES))

        user_id = int(request.query_params.get('user'))
        anonymous_name = {'anonymous_name': CITY_NAMES[user_id]}
        return Response(anonymous_name, status=status.HTTP_200_OK)
