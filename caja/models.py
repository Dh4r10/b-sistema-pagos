from django.db import models
import pytz
# Create your models here.

class Caja(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(null=False, default=True)

    class Meta:
        db_table="caja"

class TurnoCaja(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(null=False, default=True)

    class Meta:
        db_table="turno_caja"

class Apertura(models.Model):
    id_caja = models.ForeignKey(Caja,models.DO_NOTHING,db_column="id_caja", null=False, blank=False)
    id_turno_caja = models.ForeignKey(TurnoCaja,models.DO_NOTHING,db_column="id_turno_caja", null=False, blank=False)
    monto_inicial = models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False)
    fecha_apertura = models.DateTimeField(null=False, auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True,auto_now_add=True)
    estado = models.BooleanField(null=False, default=True)

    class Meta:
        db_table="apertura"

class Movimiento(models.Model):
    tipo_movimiento = models.CharField(max_length=50, null=False, blank=False)
    id_apertura = models.ForeignKey(Apertura,models.DO_NOTHING,db_column="id_apertura", null=False, blank=False)
    monto = models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False)
    total = models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False)
    fecha = models.DateTimeField(null=False, auto_now_add=True)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = "movimiento"

class AperturaMovimiento(models.Model):
    tipo_movimiento = models.CharField(max_length=50, null=False, blank=False)
    monto = models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False)
    total = models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False)
    fecha = models.DateTimeField(null=False, auto_now_add=True)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(null=False, default=True)
    id_apertura = models.BigIntegerField(null=False, blank=False,unique=True)

    class Meta:
        db_table="apertura_movimiento"

class HistorialPagos(models.Model):
    codigo=models.CharField(max_length=50,unique=True,null=True,blank=True)
    alumno=models.CharField(max_length=100,blank=True,null=True)
    tipo_de_pago=models.CharField(max_length=50,blank=True,null=True)
    monto= models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    fecha=models.DateField(blank=True,null=False)

    class Meta:
        db_table="historial_pagos"

class AperturaCaja(models.Model):
    nombre =models.CharField(max_length=50,blank=True,null=True)
    fecha_apertura = models.DateTimeField(null=False, auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True)
    estado = models.BooleanField(null=False, default=True)
    class Meta:
        db_table="apertura_caja"

