# Generated by Django 4.2.4 on 2024-07-20 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0006_aperturacaja_aperturamovimiento_historialpagos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historialpagos',
            name='id_Document',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='monto',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
