# Generated by Django 5.0.4 on 2024-04-23 15:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0055_auto_20240423_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
