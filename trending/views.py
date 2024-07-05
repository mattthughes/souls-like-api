from rest_framework import generics, permissions
from .models import Trending
from posts.models import Post
from .serializers import TrendingSerializer

# Create your views here.


class TrendingList(generics.ListAPIView):
    """
    Lists Trending posts 
    """
    serializer_class = TrendingSerializer
    queryset = Trending.objects.all()
