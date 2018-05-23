from rest_framework import serializers
from rest_framework.request import Request

from .models import (
    Campus, Course, Post, Student, Subject, Tag
)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'name',
            'campus',
        ]


class CampusSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Campus
        fields = [
            'id',
            'name',
            'courses',
        ]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = [
            'id',
            'name',
            'course',
        ]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'email',
            'password',
            'course'
        ]

        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }

    def create(self, validated_data):
        user = Student(**validated_data)
        password = validated_data['password']
        user.set_password(password)
        user.save()
        return user


class TagSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tag
        fields = [
            'id',
            'description',
            'quantity',
        ]

    def get_or_create(self):
        defaults = self.validated_data.copy()
        identifier = defaults.pop('description')
        return Tag.objects.get_or_create(description=identifier, defaults=defaults)


class PostSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'content',
            'subject',
            'tag',
            'emotion',
            'created_at',
        ]

    def __init__(self, *args, **kwargs):
        super(serializers.ModelSerializer, self).__init__(*args, **kwargs)

        request = self._get_request_from_kwargs(kwargs)

        if isinstance(request, Request):
            user = request.user
            try:
                user_id = int(request.parser_context['kwargs'].get('user_id'))
            except:  # noqa: E722
                user_id = 0

            if user.id == user_id:
                return  # The user can see his Posts content data

        # For any other user remove the content
        exclude_fields = {'content', }

        for field in exclude_fields:
            self.fields.pop(field)

    def _get_request_from_kwargs(self, kwargs):
        context = kwargs.get('context', None)

        if context is not None:
            return context.get('request', None)

        return None


class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'subject',
            'tag',
            'emotion',
            'created_at',
        ]