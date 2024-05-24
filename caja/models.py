from django.db import models

# Create your models here.

class Caja(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(null=False, default=True)



