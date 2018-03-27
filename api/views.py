from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Course, Subject
from .serializers import CourseSerializer, SubjectSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
