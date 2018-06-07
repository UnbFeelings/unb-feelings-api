# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

from api.models import Campus, Course

UserModel = get_user_model()


class UserRegistrationTestCase(APITestCase):
    def setUp(self):
        campus = Campus.objects.get_or_create(name="FGA")[0]
        self.course = Course.objects.get_or_create(
            name="ENGENHARIA", campus=campus)[0]

    def test_valid_user(self):
        """
        Test to verify if given a valid user data. It registers the user
        """
        user_data = {
            "course": self.course.id,
            "email": "test@testuser.com",
            "password": "password",
        }

        client = APIClient()
        response = client.post('/api/users/', user_data)

        # 201 == created
        self.assertEqual(201, response.status_code)
        self.assertEqual("test@testuser.com", response.data["email"])

    def test_cant_create_user_without_email(self):
        user_data = {
            "course": self.course.id,
            "password": "password",
        }

        client = APIClient()
        response = client.post('/api/users/', user_data)

        self.assertEqual(400, response.status_code)
        self.assertEqual("Este campo é obrigatório.",
                         response.data["email"][0])
