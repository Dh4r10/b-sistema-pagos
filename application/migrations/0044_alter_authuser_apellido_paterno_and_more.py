# Generated by Django 5.0.4 on 2024-04-21 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0043_alter_authuser_nombres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='apellido_paterno',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='nombres',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
