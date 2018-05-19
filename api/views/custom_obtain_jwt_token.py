from rest_framework_jwt.views import ObtainJSONWebToken
from api.models import Student


class CustomObtainJWTToken(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = \
            super(CustomObtainJWTToken, self).post(request, *args, **kwargs)

        user = Student.objects.get(email=request.data['email'])
        response.data['user'] = user.pk

        return response
