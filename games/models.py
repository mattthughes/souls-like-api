from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Game(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(
        upload_to='image/', default='../default_post_iv2gcq', blank=True
    )
    description = models.TextField(blank=True)


    def __str__(self):
        return f" {self.title}"

