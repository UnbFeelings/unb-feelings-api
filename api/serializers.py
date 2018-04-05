from rest_framework import serializers

from .models import (
    Course, Post, Student, Subject, Tag, Emotion
)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'name',
        ]
        

class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = [
            'id',
            'name',
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


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'content',
            'subject',
            'tag',
            'emotion',
        ]
