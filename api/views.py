from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Course, Subject, Tag
from .serializers import CourseSerializer, SubjectSerializer, TagSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

