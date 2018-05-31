from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, list_route
from rest_framework.response import Response

from api.serializers import PostSerializer
from api.models import Post, Student, Subject
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
                    "subject": 15,
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
                    "subject": COMBUSTIVEIS E BIOCOMBUSTIVEIS,
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
                    "subject": 11,
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
                    "subject": 15,
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
                    "subject": 15,
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
                    "subject": 15,
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
                    "subject": 15,
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
                    "subject": 15,
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
                    "subject": 15,
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
