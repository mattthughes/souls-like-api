# Generated by Django 4.2 on 2024-07-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(choices=[('DARK-SOULS-1', 'Darksouls1'), ('DARK-SOULS-2', 'Darksouls2'), ('DARK-SOULS-3', 'Darksouls3'), ('ELDEN-RING', 'Eldenring'), ('DEMONS-SOULS', 'Demonssouls'), ('BLOOD-BORNE', 'Bloodborne'), ('SEKIRO-SHADOWS-DIE-TWICE', 'Sekiroshadowsdietwice'), ('OTHER', 'Other')], max_length=24),
        ),
    ]
