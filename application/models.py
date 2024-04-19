from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AuthUser(AbstractUser):
    tipo_usuario = models.ForeignKey(
        'TipoUsuario',  
        on_delete=models.CASCADE,
        related_name='tipo_usuario',
        blank=False,
        null=False,
        default=2,
        db_column='id_tipo_usuario'
    )

    ruta_fotografia = models.CharField(max_length=255, null=False, default='https://objetivoligar.com/wp-content/uploads/2017/03/blank-profile-picture-973460_1280-580x580.jpg')
    nombres = models.CharField(max_length=50, null=False)
    apellido_paterno = models.CharField(max_length=30, null=False)
    apellido_materno = models.CharField(max_length=30, null=False)
    dni = models.CharField(max_length=8, null=False)
    celular = models.CharField(max_length=9, null=False)
    domicilio = models.CharField(max_length=50, null=False)
    sexo = models.CharField(max_length=20, null=False)
    fecha_nacimiento = models.DateField(default=None, null=False, blank=False)
    fecha_creacion = models.DateField(auto_now_add=True, null=False)
    ultimo_ingreso_fecha = models.DateField(default=None)
    ultimo_ingreso_hora = models.TimeField(default=None)
    ultimo_cierre_fecha = models.DateField(default=None)
    ultimo_cierre_hora = models.TimeField(default=None)
    # Añade estos atributos para evitar el conflicto con los atributos de AbstractUser
    last_login = None
    first_name = None
    last_name = None
    groups = None
    user_permissions = None
    date_joined = None

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50, unique=True, null=False)
    descripcion = models.CharField(max_length=100, null=False)
    estado = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 'tipo_usuario'
