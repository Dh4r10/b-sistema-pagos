from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

def upload_image(instance, filename):
    return f'images/{filename}'

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
    # ruta_fotografia=models.ImageField(upload_to=upload_image, null=False, default='images/default_img.jpg')
    ruta_fotografia=models.CharField(max_length=255, default='https://ontrust-cm.culturadelalegalidad.net/sites/default/files/participantes/profile_pics/anonimo.jpg')
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

    first_name = None
    last_name = None
    groups = None
    user_permissions = None
    date_joined= None

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

# VISTAS

class UsuariosActivos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    codigo = models.CharField(max_length=150)
    usuario = models.CharField(max_length=112)
    id_tipo_usuario = models.BigIntegerField()
    tipo = models.CharField(max_length=50)
    correo = models.CharField(max_length=254)
    ultimo_inicio = models.CharField(max_length=24)

    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table = 'usuarios_activos'

class RefreshToken(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, db_column='usuario_refreshtoken')
    token = models.TextField(unique=True)

    def __str__(self):
        return self.token
    
    class Meta:
        db_table='refresh_token'