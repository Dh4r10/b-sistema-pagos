# Generated by Django 5.0.6 on 2024-05-30 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_authuser_ruta_fotografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='ruta_fotografia',
            field=models.CharField(default='images/default_img.jpg', max_length=255),
        ),
    ]