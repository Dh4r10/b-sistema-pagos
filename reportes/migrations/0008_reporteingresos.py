# Generated by Django 5.0.6 on 2024-07-10 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0007_alter_reportemetodopago_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReporteIngresos',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=8)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=101)),
                ('grado', models.CharField(max_length=15)),
                ('seccion', models.CharField(max_length=15)),
                ('tipo_pago', models.CharField(max_length=20)),
                ('id_tipo_pago', models.IntegerField()),
                ('fecha_pago', models.DateField()),
                ('ingresos', models.DecimalField(decimal_places=2, max_digits=11)),
                ('mes', models.CharField(max_length=9)),
                ('año', models.IntegerField()),
            ],
            options={
                'db_table': 'reporte_ingresos',
                'managed': False,
            },
        ),
    ]