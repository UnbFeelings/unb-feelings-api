# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

from api.models import Campus, Course, Subject, Support
from api.tests.helpers import create_test_user, TestCheckMixin

UserModel = get_user_model()


class SupportTestCase(APITestCase, TestCheckMixin):
    @create_test_user(email="test@user.com", password="testuser")
    @create_test_user(email="test2@user.com", password="testuser2")
    def setUp(self):
        self.user_sender = UserModel.objects.get(email="test@user.com")
        self.user_receiver = UserModel.objects.get(email="test2@user.com")


        
    def test_user_create_posts(self):
        client = APIClient()
        client.login(username='test@user.com', password='testuser')

        user_sender_id = self.user_sender.id
        user_receiver_id = self.user_receiver.id

        data = {
            "message": "#VoltaRonyCoins",
        }

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client.post('/api/support/'+str(user_receiver_id)+'/', data)

        self.assertEqual(201, response.status_code)
        self.assertEqual(data["message"], response.data['message'])
        self.assertEqual(user_sender_id, response.data['student_from'])
        self.assertEqual(user_receiver_id, response.data['student_to'])


    def test_get_supports_made_by_user(self):
        client = APIClient()
        client.login(username='test@user.com', password='testuser')

        user_sender_id = self.user_sender.id
        user_receiver_id = self.user_receiver.id

        data = {
            "message": "#VoltaRonyCoins",
        }

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        client.post('/api/support/'+str(user_receiver_id)+'/', data)

        response = client.get('/api/support/from_student/', data)


        self.assertEqual(200, response.status_code)
        self.assertEqual(data["message"], response.data['results'][0]['message'])
        self.assertEqual(user_sender_id, response.data['results'][0]['student_from'])
        self.assertEqual(user_receiver_id, response.data['results'][0]['student_to'])


    def test__get_supports_made_to_user(self):
        client = APIClient()
        client.login(username='test@user.com', password='testuser')


        user_sender_id = self.user_sender.id
        user_receiver_id = self.user_receiver.id

        data = {
            "message": "#VoltaRonyCoins",
        }

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        client.post('/api/support/'+str(user_receiver_id)+'/', data)
        client.logout()
        
        client = APIClient()
        client.login(username='test2@user.com', password='testuser2')

        token = self._get_user_token("test2@user.com", "testuser2")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client.get('/api/support/to_student/', data)


        self.assertEqual(200, response.status_code)
        self.assertEqual(data["message"], response.data['results'][0]['message'])
        self.assertEqual(user_sender_id, response.data['results'][0]['student_from'])
        self.assertEqual(user_receiver_id, response.data['results'][0]['student_to'])


    def test_get_none_supports_made_by_user(self):
        client = APIClient()
        client.login(username='test@user.com', password='testuser')

        data = { }

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))

        response = client.get('/api/support/from_student/', data)


        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.data['count'])
        # self.assertEqual(user_sender_id, response.data['results'][0]['student_from'])
        # self.assertEqual(user_receiver_id, response.data['results'][0]['student_to'])

    def test_get_none_supports_made_to_user(self):
        client = APIClient()
        client.login(username='test@user.com', password='testuser')

        data = { }

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))

        response = client.get('/api/support/to_student/', data)


        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.data['count'])
    

    def test_post_support_denied_permission(self):
        client = APIClient()
        user_receiver_id = self.user_receiver.id

        data = { }

        response = client.post('/api/support/'+str(user_receiver_id)+'/', data)

        self.assertEqual(401, response.status_code)


    def test_get_support_to_student_denied_permission(self):
        client = APIClient()

        data = { }

        response = client.get('/api/support/to_student/', data)

        self.assertEqual(401, response.status_code)


    def test_get_support_from_student_denied_permission(self):
        client = APIClient()

        data = { }

        response = client.get('/api/support/from_student/', data)

        self.assertEqual(401, response.status_code)
    