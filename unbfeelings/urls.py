from api.views import (
    CampusViewSet, CourseViewSet, PostViewSet, StudentViewSet, SubjectViewSet,
    TagViewSet, EmotionViewSet
)

from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from rest_framework_jwt.views import (
    obtain_jwt_token, refresh_jwt_token
)

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='UnB Feelings API')

ROUTER = DefaultRouter()
ROUTER.register(r'courses', CourseViewSet, base_name='courses')
ROUTER.register(r'subjects', SubjectViewSet, base_name='subjects')
ROUTER.register(r'users', StudentViewSet)
ROUTER.register(r'tags', TagViewSet, base_name='tags')
ROUTER.register(r'posts', PostViewSet, base_name='posts')
ROUTER.register(r'emotions', EmotionViewSet, base_name='emotions')
ROUTER.register(r'campus', CampusViewSet, base_name='campus')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^api/', include(ROUTER.urls)),
    url(r'^api/token-auth/', obtain_jwt_token),
    url(r'^api/token-refresh/', refresh_jwt_token),
]
