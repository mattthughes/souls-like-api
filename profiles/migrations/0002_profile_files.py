# Generated by Django 4.2 on 2024-07-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='files',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]
