"""unbfeelings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CourseViewSet, SubjectViewSet, TagViewSet

ROUTER = DefaultRouter()
ROUTER.register(r'courses', CourseViewSet, base_name='courses')
ROUTER.register(r'subjects', SubjectViewSet, base_name='subjects')
ROUTER.register(r'tags', TagViewSet, base_name='tags')


urlpatterns = [
    path('', include(ROUTER.urls)),
    path('admin/', admin.site.urls),
]
