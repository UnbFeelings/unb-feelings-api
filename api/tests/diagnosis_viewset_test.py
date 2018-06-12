# -*- coding: utf-8 -*-
from datetime import timedelta

from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from django.utils import timezone

from django.test import TestCase

from api.models import Campus, Post, Course, Subject, Student, Tag
from api.tests.helpers import create_test_user
from api.views.diagnosis_views import get_last_week_posts

UserModel = get_user_model()

TODAY = timezone.now()

MONDAY = TODAY - timedelta(days=TODAY.weekday())
TUESDAY = MONDAY + timedelta(days=1)
WEDNESDAY = TUESDAY + timedelta(days=1)
THURSDAY = WEDNESDAY + timedelta(days=1)
FRIDAY = THURSDAY + timedelta(days=1)
SATURDAY = FRIDAY + timedelta(days=1)
SUNDAY = SATURDAY + timedelta(days=1)

WEEK_DAYS = [(MONDAY, 'monday'), (TUESDAY, 'tuesday'),
             (WEDNESDAY, 'wednesday'), (THURSDAY, 'thursday'),
             (FRIDAY, 'friday'), (SATURDAY, 'saturday'), (SUNDAY, 'sunday')]


class DiagnosisTestCase(APITestCase):
    @create_test_user(email="test_a@user.com", password="testuser")
    @create_test_user(email="test_b@user.com", password="testuser")
    def setUp(self):
        campus = Campus.objects.get_or_create(name="FGA")[0]
        course = Course.objects.get_or_create(
            name="ENGENHARIA", campus=campus)[0]
        self.c1 = Subject.objects.get_or_create(
            name="Calculo 1", course=course)[0]
        self.f1 = Subject.objects.get_or_create(
            name="Fisica 1", course=course)[0]
        self.user_a = UserModel.objects.get(email="test_a@user.com")
        self.user_b = UserModel.objects.get(email="test_b@user.com")

        words = ['Allahu', 'Akibar', 'deu ruim', 'ok', 'Vish', 'agora', 'vai']
        self.c1_days = []
        self.f1_days = []
        for i, word in enumerate(words):
            post = Post.objects.get_or_create(
                content=word,
                author=self.user_a if i % 2 == 0 else self.user_b,
                subject=self.c1 if i % 2 == 0 else self.f1,
                emotion="g" if i % 2 == 0 else "b")[0]

            if i % 2 == 0:
                self.c1_days.append(WEEK_DAYS[i])
            else:
                self.f1_days.append(WEEK_DAYS[i])

            post.created_at = WEEK_DAYS[i][0]
            post.save()

    def test_get_weekly_feelings_of_unb(self):
        """
        get all weekly feelings of UNB
        """
        client = APIClient()
        response = client.get("/api/diagnosis/")

        self.assertEqual(200, response.status_code)

        for day in WEEK_DAYS:
            post = Post.objects.filter(created_at=day[0]).first()
            self.assertEqual(post.id, response.data[day[1]][0]['id'])

    def test_invalid_target_raises_404_error(self):
        """
        When an invalid target is given an error 404 is returned
        """
        client = APIClient()
        response = client.get("/api/diagnosis/?target={}".format("invalid"))

        self.assertEqual(404, response.status_code)

    def test_get_posts_by_subject(self):
        client = APIClient()
        response = client.get("/api/diagnosis/?target={}&target_id={}".format(
            "subject", self.c1.id))

        self.assertEqual(200, response.status_code)

        for (day_date, day_name) in self.c1_days:
            post = Post.objects.filter(
                created_at=day_date, subject=self.c1).first()

            self.assertEqual(post.id, response.data[day_name][0]['id'])

        response = client.get("/api/diagnosis/?target={}&target_id={}".format(
            "subject", self.f1.id))

        self.assertEqual(200, response.status_code)

        for (day_date, day_name) in self.f1_days:
            post = Post.objects.filter(
                created_at=day_date, subject=self.f1).first()
            self.assertEqual(post.id, response.data[day_name][0]['id'])

    def test_get_posts_by_student(self):
        client = APIClient()
        response = client.get("/api/diagnosis/?target={}&target_id={}".format(
            "student", self.user_a.id))

        self.assertEqual(200, response.status_code)

        posts = self.user_a.posts.all()

        total_posts = 0
        for day in response.data.keys():
            total_posts += len(response.data[day])
        self.assertEqual(len(posts), total_posts)


class DiagnosisWeeklyCountTestCase(TestCase):
    @create_test_user(email="test_b@user.com", password="testuser")
    def setUp(self):
        self.setup_posts()

    def test_get_last_week_posts_with_this_week_posts(self):
        posts = get_last_week_posts()
        this_week_post_content = ['Day 1', 'Day 2', 'Day 3',]
        this_week_posts = posts.filter(content__in=this_week_post_content)

        self.assertEquals(len(this_week_post_content), this_week_posts.count())

        now = timezone.now()
        minimum_acceptable_time = timedelta(days=0)
        maximum_acceptable_time = timedelta(days=7)

        for post in this_week_posts:
            post_time = now - post.created_at
            self.assertTrue(post_time >= minimum_acceptable_time)
            self.assertTrue(post_time <= maximum_acceptable_time)

    def test_get_last_week_posts_with_out_of_week_posts(self):
        out_of_this_week_post_content = ['Day 7', 'Day 8', 'Day 9']
        out_of_this_week_posts = Post.objects.filter(content__in=out_of_this_week_post_content)
        self.assertEquals(len(out_of_this_week_post_content), out_of_this_week_posts.count())

        now = timezone.now()
        minimum_acceptable_time = timedelta(days=0)
        maximum_acceptable_time = timedelta(days=7)
        for post in out_of_this_week_posts:
            post_time = now - post.created_at
            self.assertTrue(post_time >= minimum_acceptable_time)
            self.assertTrue(post_time > maximum_acceptable_time)

        this_week_posts = get_last_week_posts()
        invalid_posts = this_week_posts.filter(content__in=out_of_this_week_post_content)
        self.assertEquals(invalid_posts.count(), 0)

    def setup_posts(self):
        student = UserModel.objects.all()[0]
        campus = Campus.objects.get_or_create(name="FGA")[0]
        course = Course.objects.get_or_create(
            name="ENGENHARIA", campus=campus)[0]

        self.c1 = Subject.objects.get_or_create(
            name="Calculo 1", course=course)[0]

        subject = Subject.objects.all()[0]

        days = 10
        for i in range(days):
            emotion = Post.EMOTIONS[i % 2][0]
            content = 'Day {}'.format(i)
            created_at = timezone.now() - timezone.timedelta(days=i)
            post = Post.objects.create(
                content=content, author=student, subject=subject,
                emotion=emotion,
                created_at=created_at)
