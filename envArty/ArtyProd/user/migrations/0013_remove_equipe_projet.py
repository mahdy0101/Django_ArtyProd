# Generated by Django 4.2 on 2023-05-06 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_equipe_projet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='Projet',
        ),
    ]
