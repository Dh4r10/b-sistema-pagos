from django.db import models

class ReporteMetodosPagos(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=8)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    grado = models.CharField(max_length=15)
    seccion = models.CharField(max_length=15)
    metodo = models.CharField(max_length=30, null=True, blank=True)
    id_metodo = models.IntegerField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()

    class Meta:
        managed = False  
        db_table = "reporte_metodo_pago"
