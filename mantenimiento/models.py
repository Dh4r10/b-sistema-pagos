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

#Filtro de area por mantenimiento    
class AreaMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table="area_mantenimiento"

#Filtro de metodo de pago por mantenimiento
class MetodoPagoMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table="metodo_pago_mantenimiento"

#Filtro de tipo de pago por mantenimiento
class TipoPagoMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table="tipo_pago_mantenimiento"

#Filtro de grado por mantenimiento
class GradoMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table="grado_mantenimiento"

#Filtro de seccion por mantenimiento
class SeccionMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table="seccion_mantenimiento"

#Filtro de seccion por mantenimiento
class ConfirmacionMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table="confirmacion_mantenimiento"

#Filtro de sexo por mantenimiento
class SexoMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table="sexo_mantenimiento"

#Filtro de turno por mantenimiento
class TurnoMantenimiento(models.Model):
    tabla=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.BooleanField(default=True)
    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table="turno_mantenimiento"

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




