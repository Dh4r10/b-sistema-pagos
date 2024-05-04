from django.db import models

# Create your models here.
class Confirguracion(models.Model):
    tabla=models.CharField(max_length=30, unique=False, null=False, blank=True)
    nombre=models.CharField(max_length=30, unique=True, null=False, blank=True)
    descripcion=models.CharField(max_length=100, unique=False, null=False,blank=True)
    estado=models.BooleanField(default=True,null=False)

    class Meta:
        db_table="configuracion"


