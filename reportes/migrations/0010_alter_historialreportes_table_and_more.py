# Generated by Django 4.2.4 on 2024-07-20 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0009_tiporeportes_permisosreportes_historialreportes'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='historialreportes',
            table='historial_reportes',
        ),
        migrations.AlterModelTable(
            name='permisosreportes',
            table='permisos_reportes',
        ),
        migrations.AlterModelTable(
            name='tiporeportes',
            table='tipo_reportes',
        ),
    ]
