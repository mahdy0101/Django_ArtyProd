# Generated by Django 4.1.7 on 2023-05-23 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0031_alter_projet_date_debut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='date_debut',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
