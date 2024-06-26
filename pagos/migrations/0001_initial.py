# Generated by Django 5.0.4 on 2024-05-16 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('monto', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('estado', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tipo_pago',
            },
        ),
    ]
