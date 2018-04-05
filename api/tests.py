from django.test import TestCase, Client
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from .models import *
from .views import *
import json

class ViewSetTest(APITestCase):
    def setUp(self):
        self.user = Student(id=1,email='abc@gmail.com', password='123456', is_superuser=True)
        self.client.force_authenticate(self.user)
    
    def tearDown(self):
        self.user.delete()
        self.client.logout()

    def test_course_view_set_get(self):
        request = APIRequestFactory().get("")
        view = CourseViewSet.as_view(actions={'get': 'retrieve'})
        course = Course.objects.create(name='Engenharia')
        response = view(request, pk=course.pk)
        self.assertEquals(response.status_code, 200)

    def test_course_view_set_list(self):
        request = APIRequestFactory().get("")
        view = CourseViewSet.as_view(actions={'get': 'list'})
        response = view(request)
        self.assertEquals(response.status_code, 200)

    def test_course_view_set_create(self):
        response = self.client.post(
            '/api/courses/',
            data = {
                    'name': 'Engenharia'
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)

    def test_course_view_set_update(self):
        factory = APIRequestFactory()
        course = Course.objects.create(name='Engenharia')
        data = {'name': 'Biologia'}
        response = self.client.put('/api/courses/1/', data)
        self.assertEquals(response.status_code, 200)
