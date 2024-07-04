from django.db import models
from games.models import Game
from django.contrib.auth.models import User


class Post(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    video = models.FileField(
        upload_to= 'videos', default='../video-place-holder_cdob9m', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'