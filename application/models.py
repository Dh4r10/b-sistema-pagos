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

    # Añade estos atributos para evitar el conflicto con los atributos de AbstractUser
    groups = None
    user_permissions = None

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50, unique=True, null=False)
    descripcion = models.CharField(max_length=100, null=False)
    estado = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 'tipo_usuario'
