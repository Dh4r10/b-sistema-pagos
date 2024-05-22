from django.db import models
from datos_alumno .models import *

# Create your models here.
class TipoPago(models.Model):
    nombre=models.CharField(max_length=20,null=True,blank=True)
    descripcion=models.CharField(max_length=50,null=True,blank=True)
    monto=models.DecimalField(max_digits=10, decimal_places=2,null=False,blank=True)
    estado=models.BooleanField(null=True,blank=True)

    class Meta:
        db_table="tipo_pago"

class CronogrmaPago(models.Model):
    anio_lectivo=models.IntegerField(null=False,blank=True)
    fecha_inicio=models.DateField(null=False, blank=True)
    fecha_fin=models.DateField(null=False, blank=True)
    descripcion=models.CharField(max_length=50,null=True,blank=True)
    areaa=models.CharField(max_length=50,null=True,blank=True)
    estado=models.BooleanField(null=True,blank=True)
    id_tipo_pago=models.ForeignKey(TipoPago,models.DO_NOTHING,db_column="id_tipo_pago", default=None, null=False, blank=True)

    class Meta:
        db_table="cronograma_pagos"

class Pendiente(models.Model):
    monto_previo=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    desc_aplicado=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    estado=models.BooleanField(null=True,blank=True)
    id_alumno=models.ForeignKey(Alumno,models.DO_NOTHING,db_column="id_alumno",default=None, null=False, blank=True)
    id_cronograma_pago=models.ForeignKey(CronogrmaPago,models.DO_NOTHING,db_column="id_cronograma_pago",default=None, null=False, blank=True)

    class Meta:
        db_table="pendiente"

class Pagos(models.Model):
    codigo_recibo=models.CharField(max_length=10, null=False,blank=True)    
    fecha_emision=models.DateField(null=True,blank=True)
    moneda=models.CharField(max_length=20,null=False,blank=True )
    condicion_venta=models.CharField(max_length=20,null=False,blank =True)
    metodo_pago=models.CharField(max_length=30,null=False,blank=True)
    cantidad=models.IntegerField(null=True,blank=True)
    um=models.CharField(max_length=10,null=False,blank=True)
    precio_unitario=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    op_exonerada=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    tasa_igv=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    anticipado=models.BooleanField(null=False,blank=True)
    estado=models.BooleanField(null=False,blank=True)
    mes_cancelado=models.CharField(max_length=50, null=True,blank=True)
    area_desaprobada=models.CharField(max_length=50, null=True,blank=True)
    id_pendiente=models.ForeignKey(Pendiente,models.DO_NOTHING,db_column="id_pendiente",default=None,null=False)
    monto=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    

    class Meta:
        db_table="pagos"



