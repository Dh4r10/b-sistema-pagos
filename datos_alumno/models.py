from django.db import models

# Upload image

def upload_image(instance, filename):
    return f'estudiantes/dni-{filename}'

# Create your models here.
class Beneficio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, unique=True, null=False, blank=True)
    descripcion = models.CharField(max_length=50, null=False, blank=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=True)
    estado = models.BooleanField(default=True, null=False, blank=True)

    class Meta:
        db_table = 'beneficio'
        indexes = [
            models.Index(fields=['nombre']),
        ]
        
class Familiar(models.Model):
    id = models.AutoField(primary_key=True)
    parentesco = models.CharField(max_length=50, null=False, blank=False)
    dni = models.CharField(max_length=8, null=False, blank=False)
    nombres = models.CharField(max_length=50, null=False, blank=False)
    apellido_paterno = models.CharField(max_length=50, null=False, blank=False)
    apellido_materno = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(max_length=10, null=False, blank=False)
    departamento_nacimiento = models.CharField(max_length=30, null=False, blank=False)
    provincia_nacimiento = models.CharField(max_length=30, null=False, blank=False)
    distrito_nacimiento = models.CharField(max_length=30, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    estado_civil = models.CharField(max_length=10, null=False, blank=False)
    vive = models.BooleanField(default=True)
    vive_con = models.BooleanField(default=True)
    apoderado = models.BooleanField(default=True)
    celular = models.CharField(max_length=9, null=False, blank=False)
    telefono = models.CharField(max_length=9, default="S/N")
    departamento_domicilio = models.CharField(max_length=30, null=False, blank=False)
    provincia_domicilio = models.CharField(max_length=30, null=False, blank=False)
    distrito_domicilio = models.CharField(max_length=30, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    grado_instruccion = models.CharField(max_length=30, null=False, blank=False)
    centro_trabajo = models.CharField(max_length=50, null=False, blank=False)
    ocupacion = models.CharField(max_length=30, null=False, blank=False)
    correo = models.CharField(max_length=50, null=False, blank=False)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = "familiar"

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    ruta_fotografia = models.ImageField(upload_to=upload_image, null=True, default='hombre.png')
    dni = models.CharField(max_length=8, null=False, blank=False)
    nombres = models.CharField(max_length=50, null=False, blank=False)
    apellido_paterno = models.CharField(max_length=50, null=False, blank=False)
    apellido_materno = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(max_length=10, null=False, blank=False)
    departamento_nacimiento = models.CharField(max_length=30, null=False, blank=False)
    provincia_nacimiento = models.CharField(max_length=30, null=False, blank=False)
    distrito_nacimiento = models.CharField(max_length=30, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    lengua_materna = models.CharField(max_length=20, null=False, blank=False)
    religion = models.CharField(max_length=20, null=False, blank=False)
    parto = models.CharField(max_length=20, null=False, blank=False)
    numero_hermanos = models.IntegerField(null=False, blank=False)
    departamento_domicilio = models.CharField(max_length=30, null=False, blank=False)
    provincia_domicilio = models.CharField(max_length=30, null=False, blank=False)
    distrito_domicilio = models.CharField(max_length=30, null=False, blank=False)
    direccion = models.CharField(max_length=20, null=False, blank=False)
    situacion = models.CharField(max_length=20, null=False, blank=False)
    cod_ie_procedencia = models.CharField(max_length=20, null=False, blank=False)
    nivel = models.CharField(max_length=15, null=False, blank=False)
    turno = models.CharField(max_length=15, null=False, blank=False)
    seccion = models.CharField(max_length=15, null=False, blank=False)
    grado = models.CharField(max_length=15, null=False, blank=False)
    id_beneficio = models.ForeignKey(Beneficio, models.DO_NOTHING, db_column="id_beneficio", null=False, blank=False)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    deuda = models.BooleanField(default=True)
    eliminacion_pendiente = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = "alumno"
        indexes = [
            models.Index(fields=['dni']),
            models.Index(fields=['nombres']),
            models.Index(fields=['apellido_paterno']),
            models.Index(fields=['apellido_materno']),
            models.Index(fields=['turno']),
            models.Index(fields=['grado']),
            models.Index(fields=['seccion']),
        ]

class AlumnoFamiliar(models.Model):
    id = models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column="id_alumno", null=False, blank=False)
    id_familiar = models.ForeignKey(Familiar, models.DO_NOTHING, db_column="id_familiar", null=False, blank=False)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = "alumno_x_familiar"
