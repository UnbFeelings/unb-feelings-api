# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

from api.models import Campus, Course, Subject, Post
from api.tests.helpers import create_test_user, TestCheckMixin

UserModel = get_user_model()


class PostTestCase(APITestCase, TestCheckMixin):
    @create_test_user(email="test@user.com", password="testuser")
    def setUp(self):
        campus = Campus.objects.get_or_create(name="FGA")[0]
        course = Course.objects.get_or_create(
            name="ENGENHARIA", campus=campus)[0]
        self.subject = Subject.objects.get_or_create(
            name="Calculo 1", course=course)[0]
        self.user = UserModel.objects.get(email="test@user.com")

        Post.objects.get_or_create(
            content="Allahu Akbar !", author=self.user,
            subject=self.subject, emotion="g")[0]

    def test_anyone_can_get_list(self):
        """
        Anyone can make get requests to list
        """
        client = APIClient()
        response = client.get('/api/posts/')
        subjects = Subject.objects.all()

        self.assertEqual(200, response.status_code)
        self.assertEqual(len(subjects), len(response.data['results']))

    def test_anyone_can_get_detail(self):
        """
        Anyone can make get requests to detail
        """
        client = APIClient()
        post = Post.objects.get(content="Allahu Akbar !")
        response = client.get('/api/posts/{}/'.format(post.id))

        self.assertEqual(200, response.status_code)
        self.assertEqual(post.id, response.data['id'])

    def test_user_create_posts(self):
        client = APIClient()

        data = {
            "content": "FooBarIsALie",
            "author": self.user.id,
            "subject": self.subject.id,
            "emotion": "b",
        }

        self._check_only_logged_user_access(
            client, lambda: client.post('/api/posts/', data))

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client.post('/api/posts/', data)

        self.assertEqual(201, response.status_code)
        self.assertEqual(data["author"], response.data['author'])
        self.assertEqual(data["subject"], response.data['subject'])
        self.assertEqual(data["emotion"], response.data['emotion'])

    def test_user_update_posts(self):
        client = APIClient()

        data = {
            "emotion": "b",
        }

        post = Post.objects.get(content="Allahu Akbar !")

        self._check_only_logged_user_access(
            client,
            lambda: client.patch('/api/posts/{}/'.format(post.id), data))

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client.patch('/api/posts/{}/'.format(post.id), data)

        self.assertEqual(200, response.status_code)
        self.assertEqual("b", response.data['emotion'])
        self.assertEqual(post.id, response.data['id'])

    def test_only_admin_can_delete(self):
        post = Post.objects.get(content="Allahu Akbar !")
        client = APIClient()

        self._check_only_logged_user_access(
            client, lambda: client.delete('/api/posts/{}/'.format(post.id)))

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client.delete('/api/posts/{}/'.format(post.id))

        self.assertEqual(204, response.status_code)
        self.assertEqual(None, response.data)
        self.assertEqual(
            0, len(Post.objects.all().filter(content="Allahu Akbar !")))

    def test_user_posts_have_content(self):
        """
        When getting post data, if it is the data from the logged user,
        content will be avalible
        """
        client = APIClient()
        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client.get('/api/posts/user/{}/'.format(self.user.id))

        self.assertEqual(200, response.status_code)
        for post in response.data['results']:
            self.assertEqual(True, 'content' in post)

    def test_user_posts_dont_have_content(self):
        """
        When getting post data, if it is not the data from the logged user,
        content will not be avalible
        """
        client = APIClient()
        response = client.get('/api/posts/user/{}/'.format(self.user.id))

        self.assertEqual(200, response.status_code)
        for post in response.data:
            self.assertEqual(False, 'content' in post)

    def test_subjects_emotions_count(self):
        """
        Subjects emotions count
        """
        client = APIClient()
        endpoint = 'api/posts/subjects_posts_count/'
        response = client.get(endpoint)

        print('\n' * 5)
        print('response = {}'.format(response))
        print('type(response) = {}'.format(type(response)))

        self.assertEqual(200, response.status_code)
        self.assertEquals(True, False)
