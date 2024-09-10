from django.db import models

# Create your models here.
class Confirguracion(models.Model):
    tabla=models.CharField(max_length=30, unique=False, null=False, blank=True)
    nombre=models.CharField(max_length=30, unique=True, null=False, blank=True)
    descripcion=models.CharField(max_length=100, unique=False, null=False,blank=True)
    estado=models.BooleanField(default=True,null=False)

    class Meta:
        db_table="configuracion"

class Auditoria(models.Model):
    tabla=models.CharField(max_length=30,null=True,blank=True)
    id_registro=models.IntegerField(null=True,blank=True)
    tabla=models.CharField(max_length=30,null=True,blank=True)
    accion=models.CharField(max_length=30,null=True,blank=True)
    fecha=models.DateField(null=True,blank=True)
    hora=models.TimeField(null=True,blank=True)
    usuario_responsable=models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        managed=False
        db_table="auditoria"




