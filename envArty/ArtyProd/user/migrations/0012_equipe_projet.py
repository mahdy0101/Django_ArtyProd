# Generated by Django 4.2 on 2023-05-06 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_personnel_ficher_cv_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='Projet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.projet'),
        ),
    ]
