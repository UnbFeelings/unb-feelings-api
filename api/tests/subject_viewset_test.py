# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

from api.models import Campus, Course, Subject
from api.tests.helpers import create_test_user

UserModel = get_user_model()


class SubjectTestCase(APITestCase):
    def setUp(self):
        campus = Campus.objects.get_or_create(name="FGA")[0]
        self.course = Course.objects.get_or_create(
            name="ENGENHARIA", campus=campus)[0]
        Subject.objects.get_or_create(name="Calculo 1", course=self.course)
        Subject.objects.get_or_create(name="CB", course=self.course)

    def test_anyone_can_get_list(self):
        """
        Anyone can make get requests to list
        """
        client = APIClient()
        response = client.get('/api/subjects/')
        subjects = Subject.objects.all()

        self.assertEqual(200, response.status_code)
        self.assertEqual(len(subjects), len(response.data['results']))

    def test_anyone_can_get_detail(self):
        """
        Anyone can make get requests to detail
        """
        client = APIClient()
        subject = Subject.objects.get(name="CB")
        response = client.get('/api/subjects/{}/'.format(subject.id))

        self.assertEqual(200, response.status_code)
        self.assertEqual(subject.id, response.data['id'])

    @create_test_user(email="test@user.com", password="testuser")
    def test_only_admin_can_create(self):
        """
        Only admin members can create new
        """
        client = APIClient()

        self._check_admin_only_access(
            client,
            lambda: client.post('/api/subjects/', {
                    "name": "A new subject", "course": self.course.id
                }),
            "test@user.com", "testuser")

        user = UserModel.objects.get(email="test@user.com")
        user.is_staff = True
        user.save()

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client.post('/api/subjects/', {
            "name": "A new subject",
            "course": self.course.id
        })

        self.assertEqual(201, response.status_code)
        self.assertEqual("A new subject", response.data['name'])

    @create_test_user(email="test@user.com", password="testuser")
    def test_only_admin_can_update(self):
        """
        Only admin members can update
        """
        subject = Subject.objects.get(name="CB")
        client = APIClient()

        self._check_admin_only_access(
            client,
            lambda: client.patch('/api/subjects/{}/'.format(subject.id), {
                        "name": "other name"
                    }),
            "test@user.com", "testuser")

        user = UserModel.objects.get(email="test@user.com")
        user.is_staff = True
        user.save()

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client.patch('/api/subjects/{}/'.format(subject.id),
                                {"name": "other name"})

        self.assertEqual(200, response.status_code)
        self.assertEqual("other name", response.data['name'])

    @create_test_user(email="test@user.com", password="testuser")
    def test_only_admin_can_delete(self):
        """
        Only admin members can delete
        """
        subject = Subject.objects.get(name="CB")
        client = APIClient()

        self._check_admin_only_access(
            client,
            lambda: client.delete('/api/subjects/{}/'.format(subject.id)),
            "test@user.com", "testuser")

        user = UserModel.objects.get(email="test@user.com")
        user.is_staff = True
        user.save()

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client.delete('/api/subjects/{}/'.format(subject.id))

        self.assertEqual(204, response.status_code)

        self.assertEqual(None, response.data)
        self.assertEqual(0, len(Subject.objects.all().filter(name="CB")))

    def _get_user_token(self, email, password):
        client = APIClient()

        response = client.post("/api/token-auth/", {
            'email': email,
            'password': password
        })

        return response.data['token']

    def _check_admin_only_access(self, client, client_action, user_email,
                                 user_password):
        response = client_action()

        self.assertEqual(401, response.status_code)
        self.assertEqual(
            "As credenciais de autenticação não foram fornecidas.",
            response.data['detail'])

        token = self._get_user_token(user_email, user_password)

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client_action()

        self.assertEqual(403, response.status_code)
        self.assertEqual("Você não tem permissão para executar essa ação.",
                         response.data['detail'])
