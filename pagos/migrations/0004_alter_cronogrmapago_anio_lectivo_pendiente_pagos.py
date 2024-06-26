# Generated by Django 5.0.4 on 2024-05-19 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos_alumno', '0006_estudiantesactivos_estudianteseliminados_and_more'),
        ('pagos', '0003_alter_cronogrmapago_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronogrmapago',
            name='anio_lectivo',
            field=models.IntegerField(blank=True),
        ),
        migrations.CreateModel(
            name='Pendiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_previo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('desc_aplicado', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('estado', models.BooleanField(blank=True, null=True)),
                ('id_alumno', models.ForeignKey(blank=True, db_column='id_alumno', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='datos_alumno.alumno')),
                ('id_cronograma_pago', models.ForeignKey(blank=True, db_column='id_cronograma_pago', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='pagos.cronogrmapago')),
            ],
            options={
                'db_table': 'pendiente',
            },
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_recibo', models.CharField(blank=True, max_length=10)),
                ('fecha_emision', models.DateField(blank=True, null=True)),
                ('moneda', models.CharField(blank=True, max_length=20)),
                ('condicion_venta', models.CharField(blank=True, max_length=20)),
                ('metodo_pago', models.CharField(blank=True, max_length=30)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('um', models.CharField(blank=True, max_length=10)),
                ('precio_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('op_exonerada', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tasa_igv', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('anticipado', models.BooleanField(blank=True)),
                ('estado', models.BooleanField(blank=True)),
                ('mes_cancelado', models.CharField(blank=True, max_length=50, null=True)),
                ('area_desaprobada', models.CharField(blank=True, max_length=50, null=True)),
                ('monto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('id_pendiente', models.ForeignKey(db_column='id_pendiente', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='pagos.pendiente')),
            ],
            options={
                'db_table': 'pagos',
            },
        ),
    ]
