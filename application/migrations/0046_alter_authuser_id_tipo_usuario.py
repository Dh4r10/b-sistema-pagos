# Generated by Django 5.0.4 on 2024-04-21 04:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0045_alter_authuser_apellido_materno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='id_tipo_usuario',
            field=models.ForeignKey(blank=True, db_column='id_tipo_usuario', on_delete=django.db.models.deletion.DO_NOTHING, to='application.tipousuario'),
        ),
    ]