from django.contrib.auth import get_user_model
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
