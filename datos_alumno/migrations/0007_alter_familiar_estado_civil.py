# Generated by Django 5.0.6 on 2024-05-19 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos_alumno', '0006_estudiantesactivos_estudianteseliminados_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='estado_civil',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
