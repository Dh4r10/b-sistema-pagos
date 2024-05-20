from django.db import models

# Create your models here.
class Confirguracion(models.Model):
    tabla=models.CharField(max_length=30, unique=False, null=False, blank=True)
    nombre=models.CharField(max_length=30, unique=True, null=False, blank=True)
    descripcion=models.CharField(max_length=100, unique=False, null=False,blank=True)
    estado=models.BooleanField(default=True,null=False)

    class Meta:
        db_table="configuracion"

#Filtro de meses por mantenimiento
class MesesMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table="meses_mantenimiento"
        
class AreaMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table="area_mantenimiento"
    
   




