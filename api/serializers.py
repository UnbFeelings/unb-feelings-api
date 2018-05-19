from rest_framework import serializers

from .models import (
    Campus, Course, Post, Student, Subject, Tag, Emotion
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


class EmotionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Emotion
        fields = [
            'id',
            'name',
            'emotion_type',
            'image_link',
        ]

    def get_name(self, obj):
        return obj.get_emotion_type_display()


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
