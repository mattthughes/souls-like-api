# Generated by Django 4.2 on 2024-08-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_game_description_game_image_game_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
