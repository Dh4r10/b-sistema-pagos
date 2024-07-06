# Generated by Django 5.0.6 on 2024-05-24 06:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0004_apertura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_movimiento', models.CharField(max_length=50)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
                ('id_apertura', models.ForeignKey(db_column='id_apertura', on_delete=django.db.models.deletion.DO_NOTHING, to='caja.apertura')),
            ],
            options={
                'db_table': 'movimiento',
            },
        ),
    ]
