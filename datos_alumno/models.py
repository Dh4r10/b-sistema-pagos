from django.db import models

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
    ruta_fotografia = models.CharField(max_length=255, default='https://objetivoligar.com/wp-content/uploads/2017/03/blank-profile-picture-973460_1280-580x580.jpg')
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

class AlumnoFamiliar(models.Model):
    id = models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column="id_alumno", null=False, blank=False)
    id_familiar = models.ForeignKey(Familiar, models.DO_NOTHING, db_column="id_familiar", null=False, blank=False)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = "alumno_x_familiar"

class EstudiantesActivos(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=8)
    deuda = models.BooleanField()
    alumno = models.CharField(max_length=152)
    beneficio = models.CharField(max_length=20)
    turno = models.CharField(max_length=15)
    grado = models.CharField(max_length=15)
    seccion = models.CharField(max_length=15)
    ruta_fotografia=models.CharField(max_length=255)
    deuda=models.BooleanField(blank=True)

    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table = "estudiantes_activos"

class EstudiantesEliminados(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=8)
    deuda = models.BooleanField()
    alumno = models.CharField(max_length=152)
    beneficio = models.CharField(max_length=20)
    turno = models.CharField(max_length=15)
    grado = models.CharField(max_length=15)
    seccion = models.CharField(max_length=15)

    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este moo
        db_table = "estudiantes_eliminados"

class EstudiantesSolicitudEliminacion(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=8)
    deuda = models.BooleanField()
    alumno = models.CharField(max_length=152)
    beneficio = models.CharField(max_length=20)
    turno = models.CharField(max_length=15)
    grado = models.CharField(max_length=15)
    seccion = models.CharField(max_length=15)

    class Meta:
        managed = False  # Indica a Django que no debe crear una tabla para este modelo
        db_table = "estudiantes_en_solicitud_eliminacion"

