from api.views import (
    CourseViewSet, PostViewSet, StudentViewSet, SubjectViewSet, TagViewSet
)

from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter


ROUTER = DefaultRouter()
ROUTER.register(r'courses', CourseViewSet, base_name='courses')
ROUTER.register(r'subjects', SubjectViewSet, base_name='subjects')
ROUTER.register(r'users', StudentViewSet)
ROUTER.register(r'tags', TagViewSet, base_name='tags')
ROUTER.register(r'posts', PostViewSet, base_name='posts')

urlpatterns = [
    url(r'^api/', include(ROUTER.urls))
]
