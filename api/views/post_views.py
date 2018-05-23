from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, list_route
from rest_framework.response import Response

from api.serializers import PostSerializer
from api.models import Post, Student
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
                    "content": "asdfasd",
                    "subject": 15,
                    "emotion":"g",
                    "tag": [
                        1
                    ]
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
            "author": pedro_1195@hotmail.com,
            "content": "Quero morrer",
            "subject": COMBUSTIVEIS E BIOCOMBUSTIVEIS,
            "emotion": "b",
            "tag": [
                TAG1,
                educacao
            ]
        }
        ```
        Response example:
        ```
        {
            "id": 2,
            "author": 1,
            "content": "Quero morrer",
            "subject": 11,
            "emotion":"b",
            "tag": [
                1,
                2
            ]
        }
        ```
        """
        response = super(PostViewSet, self).create(request)
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
            "id": 1,
            "author": 1,
            "content": "asdfasd",
            "subject": 15,
            "emotion": "g",
            "tag": [
                1
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
        {
            "id": 1,
            "author": 1,
            "content": "Melhor aula do mundo",
            "subject": 15,
            "emotion": "g",
            "tag": [
                1
            ]
        }
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
          {
              "author": hpedro1195@gmail.com,
              "content": "Pior aula do mundo",
              "subject": 15,
              "emotion": "b",
              "tag": [
                TAG1,
                educacao
              ]
          }
        }
        ```
        Response example:
        ```
        {
          {
              "id": 1,
              "author": hpedro1195@gmail.com,
              "content": "Pior aula do mundo",
              "subject": 15,
              "emotion": "b",
              "tag": [
                1,
                2
              ]
          }
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
        API endpoint that getts the posts of a given user
        ---
        Response example:
        ```
        [
          {
            "id": 1,
            "author": hpedro1195@gmail.com,
            "content": "Pior aula do mundo",
            "subject": 15,
            "emotion": "b",
            "tag": [
              1,
              2
            ]
          }
        ]
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
