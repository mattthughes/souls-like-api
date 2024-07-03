from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Game(models.Model):
    class GameChoices(models.TextChoices):
        DARKSOULS1 = 'DARK-SOULS-1'
        DARKSOULS2 = 'DARK-SOULS-2'
        DARKSOULS3 = 'DARK-SOULS-3'
        ELDENRING = 'ELDEN-RING'
        DEMONSSOULS = 'DEMONS-SOULS'
        BLOODBORNE = 'BLOOD-BORNE'
        SEKIROSHADOWSDIETWICE = 'SEKIRO-SHADOWS-DIE-TWICE'
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=24, choices=GameChoices.choices)
    

    def __str__(self):
        return f" {self.title}"