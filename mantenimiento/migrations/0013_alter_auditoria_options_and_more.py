# Generated by Django 5.0.6 on 2024-05-24 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0012_merge_0008_auditoria_0011_turnomantenimiento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auditoria',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='confirmacionmantenimiento',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='gradomantenimiento',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='metodopagomantenimiento',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='seccionmantenimiento',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='sexomantenimiento',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='tipopagomantenimiento',
            options={'managed': False},
        ),
    ]
