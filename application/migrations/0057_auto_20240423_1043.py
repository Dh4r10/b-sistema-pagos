# Generated by Django 5.0.4 on 2024-04-23 15:43
import uuid
from django.db import migrations, models

def gen_uuid(apps, schema_editor):
    AuthUser = apps.get_model("application", "AuthUser")
    for row in AuthUser.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=["uuid"])

class Migration(migrations.Migration):
    dependencies = [
        ('application', '0056_authuser_uuid'),      
    ]

    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
