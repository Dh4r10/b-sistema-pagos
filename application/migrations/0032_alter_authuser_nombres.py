# Generated by Django 5.0.4 on 2024-04-21 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0031_usuariosactivos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='nombres',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
