# Generated by Django 4.2 on 2023-05-02 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_rename_equipe_personnel_equipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='img_projet',
            field=models.ImageField(max_length=255, null=True, upload_to='media/'),
        ),
    ]