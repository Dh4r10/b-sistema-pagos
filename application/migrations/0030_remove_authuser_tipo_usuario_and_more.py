# Generated by Django 5.0.4 on 2024-04-20 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0029_remove_permisos_id_modulo_permisos_id_modulos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authuser',
            name='tipo_usuario',
        ),
        migrations.AddField(
            model_name='authuser',
            name='id_tipo_usuario',
            field=models.ForeignKey(db_column='id_tipo_usuario', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='application.tipousuario'),
        ),
    ]
