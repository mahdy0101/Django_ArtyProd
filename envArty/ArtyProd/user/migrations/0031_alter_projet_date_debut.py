# Generated by Django 4.1.7 on 2023-05-23 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0030_remove_projetutilisateur_projet_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='date_debut',
            field=models.DateField(default=datetime.timezone),
        ),
    ]