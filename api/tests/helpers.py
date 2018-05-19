from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from api.models import Campus, Course

UserModel = get_user_model()


def create_test_user(*, email: str, password: str):
    def my_decorator(target):
        def wrapper(*args, **kwds):
            campus = Campus.objects.get_or_create(name="FGA")[0]
            course = Course.objects.get_or_create(
                name="ENGENHARIA", campus=campus)[0]
            user = UserModel.objects.get_or_create(
                email=email, course=course)[0]
            user.set_password(password)
            user.save()

            return target(*args, **kwds)

        return wrapper

    return my_decorator


class AdminAccessCheckMixin():
    """
    Mixin class that adds:
        * a check to logged user only on routes
        * a check to admin only on routes
        * a get user token method
    """

    def _get_user_token(self, email, password):
        client = APIClient()

        response = client.post("/api/token-auth/", {
            'email': email,
            'password': password
        })

        return response.data['token']

    def _check_only_logged_user_access(self, client, client_action):
        response = client_action()

        self.assertEqual(401, response.status_code)
        self.assertEqual(
            "As credenciais de autenticação não foram fornecidas.",
            response.data['detail'])

    def _check_admin_only_access(self, client, client_action, user_email,
                                 user_password):
        self._check_only_logged_user_access(client, client_action)

        token = self._get_user_token(user_email, user_password)

        client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = client_action()

        self.assertEqual(403, response.status_code)
        self.assertEqual("Você não tem permissão para executar essa ação.",
                         response.data['detail'])
