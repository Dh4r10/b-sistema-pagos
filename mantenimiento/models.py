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
        db_table="meses_mantenimiento"
class AreaMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        db_table="area_mantenimiento"



class MetodoPagoMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        db_table="metodo_pago_mantenimiento"

class TipoPagoMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        db_table="tipo_pago_mantenimiento"

class GradoMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        db_table="grado_mantenimiento"


class SeccionMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        db_table="seccion_mantenimiento"

class ConfirmacionMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        db_table="confirmacion_mantenimiento"
class SexoMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        db_table="sexo_mantenimiento"

class Auditoria(models.Model):
    tabla=models.CharField(max_length=30, null=False,blank=True)
    id_registro=models.IntegerField(null=False, blank=True)
    accion=models.CharField(max_length=30, null=False, blank=True)
    fecha=models.DateField(null=False, blank=True)
    hora=models.TimeField(null=False, blank=True)
    usuario_responsable=models.CharField(max_length=50, null=False, blank=True)
    class Meta:
        db_table="auditoria"

    
   




