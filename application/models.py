from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50, unique=True, null=False, blank=True)
    descripcion = models.CharField(max_length=100, null=False, blank=True)
    estado = models.BooleanField(default=True, null=False, blank=True)

    class Meta:
        db_table = 'tipo_usuario'

class AuthUser(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='id_tipo_usuario', default=None, null=False, blank=True)
    ruta_fotografia = models.CharField(max_length=255, null=False, default='https://objetivoligar.com/wp-content/uploads/2017/03/blank-profile-picture-973460_1280-580x580.jpg')
    nombres = models.CharField(max_length=50, null=False, blank=True)
    apellido_paterno = models.CharField(max_length=30, null=False, blank=True)
    apellido_materno = models.CharField(max_length=30, null=False, blank=True)
    dni = models.CharField(max_length=8, null=False, blank=True, unique=True)
    celular = models.CharField(max_length=9, null=False, blank=True)
    domicilio = models.CharField(max_length=50, null=False, blank=True)
    sexo = models.CharField(max_length=20, null=False, blank=True)
    fecha_nacimiento = models.DateField(null=False, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True, null=False)

    last_logout = models.DateTimeField(default=None, null=True, blank=False)

    # si el usuario hace un segundo Login
    # session_id_active = models.CharField(max_length=100, null=True, blank=True) # uuid => a1b2c3d4-1234-5678-1234-56781234567 
    
    # Añade estos atributos para evitar el conflicto con los atributos de AbstractUser
    # last_login = None
    first_name = None
    last_name = None
    groups = None
    user_permissions = None
    date_joined = None

#Tabla de Modulos
class Modulos(models.Model):
    nombre= models.CharField(max_length=50, unique=True, null=False, blank=True)
    descripcion=models.CharField(max_length=100, null=False, blank=True)
    estado= models.BooleanField(default=True, null=False)

    class Meta:
        db_table ="modulos"

#Tabla de Perimisos

class Permisos(models.Model):
    nombre=models.CharField(max_length=50, null=False, blank=True)
    descripcion=models.CharField(max_length=100, null=False, blank=True)
    estado=models.BooleanField(default=True, null=False)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='id_tipo_usuario',default=None, null=False, blank=True)
    id_modulos= models.ForeignKey(Modulos, models.DO_NOTHING, db_column="id_modulos", default=None, null=False, blank=True)

    class Meta:
        db_table="permisos"

#VISTAS

class UsuariosActivos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    codigo = models.CharField(max_length=150)
    usuario = models.CharField(max_length=112)
    id_tipo_usuario = models.BigIntegerField()
    tipo = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    ultimo_ingreso_fecha = models.DateField()
    ultimo_ingreso_hora = models.TimeField()
    ultimo_cierre_fecha = models.DateField()
    ultimo_cierre_hora = models.TimeField()
    is_active = models.BooleanField()

    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table = 'usuarios_activos'
