from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

from api.models import Student, Campus, Course
from api.tests.helpers import create_test_user, TestCheckMixin


UserModel = get_user_model()

class BlockTestCase(APITestCase, TestCheckMixin):
    @create_test_user(email="test@user.com", password="testuser")
    def setUp(self):
        campus = Campus.objects.get_or_create(name="FGA")[0]
        course = Course.objects.get_or_create(
            name="ENGENHARIA", campus=campus)[0]
        self.user = Student.objects.get(email="test@user.com")
        self.user2 = Student.objects.create(email='oi@oi.com',password='1', course=course)
        self.user3 = Student.objects.create(email='io@io.com',password='1', course=course)
        self.user4 = Student.objects.create(email='ii@ii.com',password='1', course=course)

    def test_user_block_user(self):
        client = APIClient()

        data = {
            "blocked": self.user2.id,
        }

        self._check_only_logged_user_access(
            client, lambda: client.post('/api/block/', data))

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client.post('/api/block/', data)

        self.assertEqual(201, response.status_code)
        self.assertEqual(self.user.id, response.data['blocker'])
        self.assertEqual(data["blocked"], response.data['blocked'])
