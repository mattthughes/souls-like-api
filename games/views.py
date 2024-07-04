from rest_framework import generics, permissions
from .models import Game
from django.contrib.auth.mixins import PermissionRequiredMixin
from .serializers import GameSerializer
from souls_like_api.permissions import IsOwnerOrReadOnly

# Create your views here.


class GameList(generics.ListAPIView):
    """
    List games view
    """
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Game.objects.all()

    

    

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a Game and edit or delete it if you own it.
    """
    serializer_class = GameSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Game.objects.all()


class CreateGame(generics.CreateAPIView):
    """
    Create view is using the game serializer
    and the permission class of is admin
    checking to see if the user making the request
    has admin privileges if they do the create view
    will load otherwise an access denied message will
    load
    """
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)