# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

from api.models import Campus, Course, Subject, Post, Emotion
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
        self.emotion = Emotion.objects.get_or_create(
            emotion_type="b",
            name="""
                Bad for BAD database design...
                Emotion should be a Post choice not a ForeignKey.
                When no one's watching I'm gonna fix this shit.
                """,
            image_link="#baddesignchoices")[0]

        self.user = UserModel.objects.get(email="test@user.com")

        p1 = Post.objects.get_or_create(
            content="Allahu Akbar !", author=self.user,
            subject=self.subject)[0]
        p1.emotion.add(self.emotion)
        p1.save()

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
            "emotion": [self.emotion.id]
        }

        self._check_only_logged_user_access(
            client, lambda: client.post('/api/posts/', data))

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client.post('/api/posts/', data)

        self.assertEqual(201, response.status_code)
        self.assertEqual("FooBarIsALie", response.data['content'])

    def test_user_update_posts(self):
        client = APIClient()

        data = {
            "content": "Other content",
        }

        post = Post.objects.get(content="Allahu Akbar !")

        self._check_only_logged_user_access(
            client,
            lambda: client.patch('/api/posts/{}/'.format(post.id), data))

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client.patch('/api/posts/{}/'.format(post.id), data)

        self.assertEqual(200, response.status_code)
        self.assertEqual("Other content", response.data['content'])
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
