from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from souls_like_api.permissions import IsOwnerOrReadOnly
from posts.models import Post
from posts.serializers import PostSerializer

# Create your views here.


class TrendingList(generics.ListAPIView):
    """
    Lists Trending posts using the post model
    to order posts by there like count the order
    will change depending on the number of likes
    users can still search by the game title to
    find posts that are useful to them.
    """
    serializer_class = PostSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-likes_count')
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',
    ]
    search_fields = [
        'game__title'
    ]


    """
    This function is limiting the posts of the post model to
    only show 10 on the page allowing only the top liked posts
    to appear on the trending page.
    """
    def finalize_response(self, request, response, *args, **kwargs):
        if response.status_code == 200:
            response.data = response.data[:10]
            return super().finalize_response(request, response, *args, **kwargs)
    

class TrendingPostDetail(generics.RetrieveAPIView):
    """
    Retrieve a trending post.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-likes_count')