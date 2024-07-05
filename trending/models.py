from django.db import models
from posts.models import Post

# Create your models here.

class Trending(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post}'