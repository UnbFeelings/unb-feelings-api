from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

from api.models import Student, Campus, Course, Block
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
        self.block = Block.objects.get_or_create(blocker=self.user, blocked=self.user3)

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

    def test_user_delete_block(self):
        client = APIClient()

        blocked_id = self.block[0].blocked.id
        self._check_only_logged_user_access(
            client, lambda: client.delete('/api/block/' + str(blocked_id) + '/'))

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client.delete('/api/block/' + str(blocked_id) + '/')

        self.assertEqual(204, response.status_code)
        self.assertEqual(None, response.data)

    def test_user_list_block(self):
        client = APIClient()

        self._check_only_logged_user_access(
            client, lambda: client.get('/api/block/'))

        token = self._get_user_token("test@user.com", "testuser")

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client.get('/api/block/')

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.data["count"])
        self.assertEqual(self.block[0].blocker.id,response.data["results"][0]["blocker"])
        self.assertEqual(self.block[0].blocked.id,response.data["results"][0]["blocked"])
