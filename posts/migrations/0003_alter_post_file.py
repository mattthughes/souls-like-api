# Generated by Django 4.2 on 2024-07-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_video_post_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, default='../video-place-holder_cdob9m', upload_to='files'),
        ),
    ]
