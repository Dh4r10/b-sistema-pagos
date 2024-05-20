from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Beneficio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, unique=True, null=False, blank=True)
    descripcion = models.CharField(max_length=50, null=False, blank=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=True)
    estado = models.BooleanField(default=True, null=False, blank=True)

    class Meta:
        db_table = 'beneficio'
        
class Familiar(models.Model):
    id = models.AutoField(primary_key=True)
    parentesco = models.CharField(max_length=50, null=False, blank=True)
    dni = models.CharField(max_length=8, null=False, blank=True)
    nombres = models.CharField(max_length=50, null=False, blank=True)
    apellido_paterno = models.CharField(max_length=50, null=False, blank=True)
    apellido_materno = models.CharField(max_length=50, null=False, blank=True)
    sexo = models.CharField(max_length=10, null=False, blank=True)
    departamento_nacimiento = models.CharField(max_length=30, null=False, blank=True)
    provincia_nacimiento = models.CharField(max_length=30, null=False, blank=True)
    distrito_nacimiento = models.CharField(max_length=30, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=True)
    estado_civil = models.CharField(max_length=10, null=False, blank=True)
    vive = models.BooleanField(default=True, null=False, blank=True)
    vive_con = models.BooleanField(default=True, null=False, blank=True)
    apoderado = models.BooleanField(default=True, null=False, blank=True)
    celular = models.CharField(max_length=9, null=False, blank=True)
    telefono = models.CharField(max_length=9, default="S/N", null=False, blank=True)
    departamento_domicilio = models.CharField(max_length=30, null=False, blank=True)
    provincia_domicilio = models.CharField(max_length=30, null=False, blank=True)
    distrito_domicilio = models.CharField(max_length=30, null=False, blank=True)
    direccion = models.CharField(max_length=50, null=False, blank=True)
    grado_instruccion = models.CharField(max_length=30, null=False, blank=True)
    centro_trabajo = models.CharField(max_length=50, null=False)
    ocupacion = models.CharField(max_length=30, null=False, blank=True)
    correo = models.CharField(max_length=50, null=False, blank=True)
    estado = models.BooleanField(default=True, null=False, blank=True)

    class Meta:
        db_table = "familiar"

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    ruta_fotografia = models.CharField(max_length=255, default='https://objetivoligar.com/wp-content/uploads/2017/03/blank-profile-picture-973460_1280-580x580.jpg', null=False, blank=True)
    dni = models.CharField(max_length=8, null=False, blank=True)
    nombres = models.CharField(max_length=50, null=False, blank=True)
    apellido_paterno = models.CharField(max_length=50, null=False, blank=True)
    apellido_materno = models.CharField(max_length=50, null=False, blank=True)
    sexo = models.CharField(max_length=10, null=False, blank=True)
    departamento_nacimiento = models.CharField(max_length=30, null=False, blank=True)
    provincia_nacimiento = models.CharField(max_length=30, null=False, blank=True)
    distrito_nacimiento = models.CharField(max_length=30, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=True)
    lengua_materna = models.CharField(max_length=20, null=False, blank=True)
    religion = models.CharField(max_length=20, null=False, blank=True)
    parto = models.CharField(max_length=20, null=False, blank=True)
    numero_hermanos = models.IntegerField(null=False, blank=True)
    departamento_domicilio = models.CharField(max_length=30, null=False, blank=True)
    provincia_domicilio = models.CharField(max_length=30, null=False, blank=True)
    distrito_domicilio = models.CharField(max_length=30, null=False, blank=False)
    direccion = models.CharField(max_length=20, null=False, blank=True)
    situacion = models.CharField(max_length=20, null=False, blank=True)
    cod_ie_procedencia = models.CharField(max_length=20, null=False, blank=True)
    nivel = models.CharField(max_length=15, null=False, blank=True)
    turno = models.CharField(max_length=15, null=False, blank=True)
    seccion = models.CharField(max_length=15, null=False, blank=True)
    grado = models.CharField(max_length=15, null=False, blank=True)
    id_beneficio = models.ForeignKey(Beneficio, models.DO_NOTHING, db_column="id_beneficio", null=False, blank=True)
    fecha_inscripcion = models.DateField(auto_now_add=True, null=False, blank=True)
    deuda = models.BooleanField(default=True, null=False, blank=True)
    eliminacion_pendiente = models.BooleanField(default=False, null=False, blank=True)
    estado = models.BooleanField(default=True, null=False, blank=True)

    class Meta:
        db_table = "alumno"

class AlumnoFamiliar(models.Model):
    id = models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column="id_alumno", null=False, blank=True)
    id_familiar = models.ForeignKey(Familiar, models.DO_NOTHING, db_column="id_familiar", null=False, blank=True)
    estado = models.BooleanField(default=True, null=False,blank=True)

    class Meta:
        db_table = "alumno_x_familiar"

class EstudiantesActivos(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=8)
    estado = models.BooleanField()
    alumno = models.CharField(max_length=152)
    beneficio = models.CharField(max_length=20)
    turno = models.CharField(max_length=15)
    grado = models.CharField(max_length=15)
    seccion = models.CharField(max_length=15)

    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table = "estudiantes_activos"

class EstudiantesEliminados(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=8)
    estado = models.BooleanField()
    alumno = models.CharField(max_length=152)
    beneficio = models.CharField(max_length=20)
    turno = models.CharField(max_length=15)
    grado = models.CharField(max_length=15)
    seccion = models.CharField(max_length=15)

    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table = "estudiantes_eliminados"

class EstudiantesSolicitudEliminacion(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=8)
    estado = models.BooleanField()
    alumno = models.CharField(max_length=152)
    beneficio = models.CharField(max_length=20)
    turno = models.CharField(max_length=15)
    grado = models.CharField(max_length=15)
    seccion = models.CharField(max_length=15)

    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table = "estudiantes_en_solicitud_eliminacion"

