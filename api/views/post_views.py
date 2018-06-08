from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import list_route
from rest_framework.response import Response

from api.serializers import PostSerializer, SubjectEmotionsCountSerializer
from api.models import Post, Student, Subject, SubjectEmotionsCount, Tag
from api.permissions import PostPermission


class PostViewSet(ModelViewSet):
    """Description: PostViewSet.

    API endpoint that allows posts to be viewed, created, deleted or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PostPermission, )

    def list(self, request):
        """
        API endpoint that allows all posts to be viewed.
        ---
        Response example:
        ```
        {
            "count": 1,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": 1,
                    "author": 1,
                    "subject": {
                        "id": 15,
                        "name": "Calculo 1",
                        "course": 1
                    },
                    "tag": [
                        {
                            "id": 1,
                            "description": "TAG1",
                            "quantity": 2
                        }
                    ],
                    "emotion":"g",
                    "created_at": "2018-05-23T00:20:22.344509Z"
                }
            ]
        }
        ```
        """
        response = super(PostViewSet, self).list(request)
        return response

    def create(self, request):
        """
        API endpoint that allows posts to be created.
        ---
        Body example:
        ```
        {
            "count": 1,
            "next": null,
            "previous": null,
            "results": [
                {
                    "author": pedro_1195@hotmail.com,
                    "subject": 1,
                    "tag": [
                            {
                                "id": 1,
                                "description": "TAG1",
                                "quantity": 2
                            }
                    ],
                    "emotion": "b",
                    "created_at": "2018-05-23T00:20:22.344509Z"
                }
            ]
        }
        ```
        Response example:
        ```
        {
            "count": 1,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": 2,
                    "author": 1,
                    "subject": {
                        "id": 1,
                        "name": "Calculo 1",
                        "course": 1
                    },
                    "tag": [
                            {
                                "id": 1,
                                "description": "TAG1",
                                "quantity": 2
                            }
                    ],
                    "emotion":"b",
                    "created_at": "2018-05-23T00:20:22.344509Z"
                }
            ]
        }
        ```
        """
        response = super(PostViewSet, self).create(request)

        if not response.data.get('created_at', None):
            return response

        post = Post.objects.get(pk=response.data.get('id'))
        tags = request.data.get('tags', "")
        response.data['tag'] = []

        for tag_text in tags.split('#'):
            description = tag_text.strip().replace(',', "")

            if len(tag_text) > 0:
                tag, created = Tag.objects.get_or_create(
                    description=description)
                post.tag.add(tag)
                post.save()
                response.data['tag'].append(tag.id)

        return response

    def destroy(self, request, pk=None):
        """
        API endpoint that allows posts to be deleted.
        """
        response = super(PostViewSet, self).destroy(request, pk)
        return response

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows a specific post to be viewed.
        ---
        Response example:
        ```
        {
            "count": 1,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": 1,
                    "author": 1,
                     "subject": {
                        "id": 15,
                        "name": "Calculo 1",
                        "course": 1
                    },
                    "tag": [
                            {
                                "id": 1,
                                "description": "TAG1",
                                "quantity": 2
                            }
                    ],
                    "emotion": "g",
                    "created_at": "2018-05-23T00:20:22.344509Z"
                }
            ]
        }
        ```
        """
        response = super(PostViewSet, self).retrieve(request, pk)
        return response

    def partial_update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a post to be partial edited.
        ---
        Body example:
        ```
        {
            "content": "Melhor aula do mundo",
        }
        ```
        Response example:
        ```
        {
            "count": 1,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": 1,
                    "author": 1,
                    "content": "Melhor aula do mundo",
                     "subject": {
                        "id": 15,
                        "name": "Calculo 1",
                        "course": 1
                    },
                    "tag": [
                            {
                                "id": 1,
                                "description": "TAG1",
                                "quantity": 2
                            }
                    ],
                    "emotion": "g",
                    "created_at": "2018-05-23T00:20:22.344509Z"
                }
            ]
        }

        ```
        """
        response = \
            super(PostViewSet, self).partial_update(request, pk, **kwargs)
        return response

    def update(self, request, pk=None, **kwargs):
        """
        API endpoint that allows a post to be edited.
        ---
        Body example:
        ```
          {
              "count": 1,
              "next": null,
              "previous": null,
              "results": [
                {
                    "author": hpedro1195@gmail.com,
                    "content": "Pior aula do mundo",
                     "subject": {
                        "id": 15,
                        "name": "Calculo 1",
                        "course": 1
                    },
                    "tag": [
                            {
                                "id": 1,
                                "description": "TAG1",
                                "quantity": 2
                            }
                    ],
                    "emotion": "b",
                    "created_at": "2018-05-23T00:20:22.344509Z"
                }
              ]
          }

        ```
        Response example:
        ```
          {
              "count": 1,
              "next": null,
              "previous": null,
              "results": [
                {
                    "id": 1,
                    "author": hpedro1195@gmail.com,
                    "content": "Pior aula do mundo",
                     "subject": {
                        "id": 15,
                        "name": "Calculo 1",
                        "course": 1
                    },
                    "tag": [
                            {
                                "id": 1,
                                "description": "TAG1",
                                "quantity": 2
                            }
                    ],
                    "emotion": "b",
                    "created_at": "2018-05-23T00:20:22.344509Z"
                }
              ]
          }

        ```
        """
        response = super(PostViewSet, self).update(request, pk, **kwargs)
        return response

    @list_route(
        permission_classes=[],
        methods=['GET'],
        url_path='user/(?P<user_id>\d+)')
    def user_posts(self, request, user_id=None):
        """
        API endpoint that gets the posts of a given user
        ---
        The "content" camp don't show up if you're not the loged user
        ---
        Response example:
        ```

          {
            "count": 1,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": 1,
                    "author": hpedro1195@gmail.com,
                    "content": "Pior aula do mundo",
                     "subject": {
                        "id": 15,
                        "name": "Calculo 1",
                        "course": 1
                    },
                    "tag": [
                            {
                                "id": 1,
                                "description": "TAG1",
                                "quantity": 2
                            }
                    ],
                    "emotion": "b",
                    "created_at": "2018-05-23T00:20:22.344509Z"
                }
            ]
          }

        ```
        """
        user = get_object_or_404(Student, pk=user_id)
        posts = Post.objects.all().filter(author=user)
        posts_paginated = self.paginate_queryset(posts)

        if posts_paginated is not None:
            serializer = PostSerializer(
                data=posts_paginated, many=True, context={'request': request})

            serializer.is_valid()
            return self.get_paginated_response(serializer.data)
        else:

            data = PostSerializer(
                data=posts, many=True, context={'request': request})

            data.is_valid()
            return Response(data.data)

    @list_route(
        permission_classes=[],
        methods=['GET'],
        url_path='subject/(?P<subject_id>\d+)')
    def subject_posts(self, request, subject_id=None):
        """
        API endpoint that getts the posts of a given subject
        ---
        Response example:
        ```
          {
            "count": 1,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": 1,
                    "author": hpedro1195@gmail.com,
                     "subject": {
                        "id": 15,
                        "name": "Calculo 1",
                        "course": 1
                    },
                    "tag": [
                            {
                                "id": 1,
                                "description": "TAG1",
                                "quantity": 2
                            }
                    ],
                    "emotion": "b",
                    "created_at": "2018-05-23T00:20:22.344509Z"
                }
            ]
          }

        ```
        """
        subject = get_object_or_404(Subject, pk=subject_id)
        posts = Post.objects.all().filter(subject=subject)
        posts_paginated = self.paginate_queryset(posts)

        if posts_paginated is not None:
            serializer = PostSerializer(
                data=posts_paginated, many=True, context={'request': request})

            serializer.is_valid()
            return self.get_paginated_response(serializer.data)
        else:

            data = PostSerializer(
                data=posts, many=True, context={'request': request})

            data.is_valid()
            return Response(data.data)

    @list_route(
        permission_classes=[],
        methods=['GET'],
        url_path='subjects_posts_count')
    def subjects_posts(self, request):
        """
        Returns posts's emotion counting for all subjects that have at least
        one post about it
        ---
        Response example:
        ```
        [
          {
            "subject_name": Calculo 1,
            "good_count": 13,
            "good_count": 2,
          }
        ]
        ```
        """

        subjects_emotions_count_list = []
        for subject in Subject.objects.all():
            emotion_count = get_subject_emotions_count(subject)
            if not emotion_count.empty():
                subjects_emotions_count_list.append(emotion_count)

        serializer = SubjectEmotionsCountSerializer(
            subjects_emotions_count_list, many=True)
        return Response(serializer.data)


def get_subject_emotions_count(subject):
    assert isinstance(subject, Subject)

    subject_posts = Post.objects.filter(subject=subject)
    subject_emotions = [post.emotion for post in subject_posts]

    from collections import Counter

    count = Counter(subject_emotions)

    for emotion_choice in Post.EMOTIONS:
        emotion = emotion_choice[0]
        if emotion not in count:
            count[emotion] = 0

    subject_emotions_count = SubjectEmotionsCount(
        subject.name, good_count=count['g'], bad_count=count['b'])

    return subject_emotions_count
