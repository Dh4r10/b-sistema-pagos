# Generated by Django 5.0.4 on 2024-04-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0058_auto_20240423_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='dni',
            field=models.CharField(blank=True, max_length=8, unique=True),
        ),
    ]
