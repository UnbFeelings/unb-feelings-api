from rest_framework_jwt.views import ObtainJSONWebToken
from api.models import Student


class CustomObtainJWTToken(ObtainJSONWebToken):
    """Description: StudentViewSet.

    API endpoint that provides the authentication token.
    """
    def post(self, request, *args, **kwargs):
        """
        API endpoint that provides an authentication token when a user enters
        the correct credentials.
        """
        response = \
            super(CustomObtainJWTToken, self).post(request, *args, **kwargs)

        user = Student.objects.get(email=request.data['email'])
        response.data['user'] = user.pk

        return response
