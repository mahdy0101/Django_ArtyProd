# Generated by Django 4.1.7 on 2023-05-22 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_remove_projetutilisateur_date_debut_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projetutilisateur',
            name='projet',
        ),
        migrations.AddField(
            model_name='projetutilisateur',
            name='projet',
            field=models.ManyToManyField(to='user.projet'),
        ),
    ]
