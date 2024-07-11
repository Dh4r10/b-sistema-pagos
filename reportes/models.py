from django.db import models

# Create your models here.

class ReporteBeneficiados(models.Model):
    id = models.IntegerField(primary_key=True)
    dni = models.CharField(max_length=8)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=101)
    grado = models.CharField(max_length=15)
    seccion = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    beneficio = models.CharField(max_length=20)
    descuento = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table = "reporte_beneficiados"

class ReporteDeudas(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dni = models.CharField(max_length=8)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=101)
    grado = models.CharField(max_length=15)
    seccion = models.CharField(max_length=15)
    nombre = models.CharField(max_length=20)
    deuda = models.DecimalField(max_digits=11,decimal_places=2)
    id_tipo_pago = models.IntegerField()

    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table = "reporte_deudas"

class ReporteMetodoPago(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dni = models.CharField(max_length=8)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=101)
    grado = models.CharField(max_length=15)
    seccion = models.CharField(max_length=15)
    metodo = models.CharField(max_length=30)
    id_metodo = models.BigIntegerField()
    monto = models.DecimalField(max_digits=10,decimal_places=2)
    fecha_vencimiento = models.DateField()

    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table = "reporte_metodo_pago"

class ReporteIngresos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dni = models.CharField(max_length=8)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=101)
    grado = models.CharField(max_length=15)
    seccion = models.CharField(max_length=15)
    tipo_pago = models.CharField(max_length=20)
    id_tipo_pago = models.IntegerField()
    fecha_pago = models.DateField()
    ingresos = models.DecimalField(max_digits=11,decimal_places=2)
    mes = models.CharField(max_length=9)
    año = models.IntegerField()

    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table = "reporte_ingresos"



