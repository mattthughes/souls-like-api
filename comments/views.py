from django.db.models import Count
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from souls_like_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List Comments can create a comment if
    authenticated this will also linked
    the logged in user to the comments id
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, if the comment owner is
    logged in they can edit or delete there comment
    """
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()