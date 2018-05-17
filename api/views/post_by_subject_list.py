from rest_framework.generics import ListAPIView

from api.serializers import PostSerializer
from api.models import Post


class PostBySubjectList(ListAPIView):
    """
    API endpoint that allows a few posts based on a subject.
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
                "subject": 1,
                "tag": [
                    1
                ]
            },
            {
                "id": 2,
                "author": 2,
                "content": "asdfasd",
                "subject": 1,
                "tag": [
                    1
                ]
            }
        ]
    }
    ```
    """

    serializer_class = PostSerializer

    def get_queryset(self):
        """

        """

        queryset = Post.objects.all()
        subject = self.request.query_params.get('pk', None)
        if subject is not None:
            queryset = queryset.filter(subject=subject)
        return queryset
