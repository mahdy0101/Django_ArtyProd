# Generated by Django 4.2 on 2023-05-06 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_alter_projet_equipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='personnels',
            field=models.ManyToManyField(null=True, to='user.personnel'),
        ),
    ]
