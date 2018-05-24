# -*- coding: utf-8 -*-
from datetime import timedelta

from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from django.utils import timezone

from api.models import Campus, Post, Course, Subject
from api.tests.helpers import create_test_user

UserModel = get_user_model()

TODAY = timezone.now()

MONDAY = TODAY - timedelta(days=TODAY.weekday())
TUESDAY = MONDAY + timedelta(days=1)
WEDNESDAY = TUESDAY + timedelta(days=1)
THURSDAY = WEDNESDAY + timedelta(days=1)
FRIDAY = THURSDAY + timedelta(days=1)
SATURDAY = FRIDAY + timedelta(days=1)
SUNDAY = SATURDAY + timedelta(days=1)

WEEK_DAYS = [
    (MONDAY, 'monday'),
    (TUESDAY, 'tuesday'),
    (WEDNESDAY, 'wednesday'),
    (THURSDAY, 'thursday'),
    (FRIDAY, 'friday'),
    (SATURDAY, 'saturday'),
    (SUNDAY, 'sunday')
]


class DiagnosisTestCase(APITestCase):
    @create_test_user(email="test@user.com", password="testuser")
    def setUp(self):
        campus = Campus.objects.get_or_create(name="FGA")[0]
        course = Course.objects.get_or_create(
            name="ENGENHARIA", campus=campus)[0]
        self.c1 = Subject.objects.get_or_create(
            name="Calculo 1", course=course)[0]
        self.f1 = Subject.objects.get_or_create(
            name="Fisica 1", course=course)[0]
        self.user = UserModel.objects.get(email="test@user.com")

        words = ['Allahu', 'Akibar', 'deu ruim', 'ok', 'Vish', 'agora', 'vai']
        for i, word in enumerate(words):
            post = Post.objects.get_or_create(
                content=word,
                author=self.user,
                subject=self.c1 if i % 2 == 0 else self.f1,
                emotion="g" if i % 2 == 0 else "b")[0]

            post.created_at = WEEK_DAYS[i][0]
            post.save()

    def test_get_weekly_feelings_of_unb(self):
        """
        get all weekly feelings of UNB
        """
        client = APIClient()
        response = client.get("/api/diagnosis/{}/".format("unb"))

        self.assertEqual(200, response.status_code)

        for day in WEEK_DAYS:
            post = Post.objects.filter(created_at=day[0]).first()
            self.assertEqual(post.id, response.data[day[1]][0]['id'])
