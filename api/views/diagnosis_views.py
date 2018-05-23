from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import datetime, timedelta

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import PostSerializer, DiagnosisSerializer
from api.models import Post, Subject


class DiagnosisViewSet(ModelViewSet):
	"""Description: DiagnosisViewSet.
	API endpoint that allows getting a diagnosis of a student, subject or university.
	"""
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	@api_view(['GET'])
	def subject_diagnosis(request, subject_id):
		"""
		API endpoint that allows getting a diagnosis of a subject
		---
		Response example:
		```
		```
		"""
		subject = get_object_or_404(Subject, pk=subject_id)

		# only posts from the last week
		posts = Post.objects.all().filter(
			subject=subject, created_at__gt=timezone.now()-timedelta(days=8)
		)

		diagnosis = {
			"sunday": posts.filter(created_at__week_day=1).values(),
			"monday": posts.filter(created_at__week_day=2).values(),
			"tuesday": posts.filter(created_at__week_day=3).values(),
			"wednesday": posts.filter(created_at__week_day=4).values(),
			"thursday": posts.filter(created_at__week_day=5).values(),
			"friday": posts.filter(created_at__week_day=6).values(),
			"saturday": posts.filter(created_at__week_day=7).values(),
		}

		return Response(diagnosis)
