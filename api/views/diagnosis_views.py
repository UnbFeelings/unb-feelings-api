from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import Http404
from datetime import timedelta

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Post, Subject, Student


class DiagnosisViewSet(ModelViewSet):
    """
    Description: DiagnosisViewSet.
    API endpoint that allows getting a diagnosis of a student, subject
    or university.
    """

    @api_view(['GET'])
    def diagnosis(request):
        """
        API endpoint that allows getting a diagnosis of a student, subject or
        university.

        By default it will return the unb feelings.
        But by using query params target and target_id it will return
        student and subject feelings.

        * /api/diagnosis/ --> unb feelings
        * /api/diagnosis/?target=student&target_id=5 --> student feelings
        * /api/diagnosis/?target=subject&target_id=7 --> subject feelings

        ---
        Response example:
        ```
        {
            "sunday": [],
            "monday": [],
            "tuesday": [
                {
                    "id": 1,
                    "author_id": 3,
                    "subject_id": 262,
                    "emotion": "g",
                    "created_at": "2018-05-23T00:20:22.344509Z"
                }
            ],
            "wednesday": [],
            "thursday": [],
            "friday": [],
            "saturday": []
        }
        ```
        """
        target = request.query_params.get("target", None)
        target_id = request.query_params.get("target_id", None)

        # only posts from the last week
        posts = get_posts_by_target(target, target_id)

        diagnosis = {
            "sunday": posts.filter(created_at__week_day=1).values(),
            "monday": posts.filter(created_at__week_day=2).values(),
            "tuesday": posts.filter(created_at__week_day=3).values(),
            "wednesday": posts.filter(created_at__week_day=4).values(),
            "thursday": posts.filter(created_at__week_day=5).values(),
            "friday": posts.filter(created_at__week_day=6).values(),
            "saturday": posts.filter(created_at__week_day=7).values(),
        }

        # I didn't found a way to remove a column right on query
        # So this is workaround to remove "content" from the posts
        for day in diagnosis.keys():
            new_day = map(lambda post: {
                    k: post[k] for k in post.keys() if k != "content"
                },
                diagnosis[day])

            diagnosis[day] = list(new_day)

        return Response(diagnosis)


def get_posts_by_target(target=None, target_id=None):
    """
    Given a target and its id, it returns the target posts on the week
    raises 404 error when target not found or target is invalid.

    Valid targets:
        * subject
        * student
        * unb
    """
    if target is None:  # is no target is given, return all unb feelings
        return Post.objects.all().filter(
            created_at__gt=timezone.now() - timedelta(days=8))

    if target == 'subject':
        subject = get_object_or_404(Subject, pk=target_id)

        return Post.objects.all().filter(
            subject=subject, created_at__gt=timezone.now() - timedelta(days=8))

    if target == 'student':
        student = get_object_or_404(Student, pk=target_id)

        return Post.objects.all().filter(
            author=student, created_at__gt=timezone.now() - timedelta(days=8))

    # if an invalid target is given return an 404 response
    raise Http404
