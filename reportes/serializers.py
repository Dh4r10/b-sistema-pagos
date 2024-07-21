from .models import ReporteBeneficiados, ReporteDeudas, ReporteMetodoPago, ReporteIngresos, TipoReportes, HistorialReportes, PermisosReportes
from application.models import AuthUser
from rest_framework.serializers import ModelSerializer, Serializer, CharField, DateField, DecimalField, IntegerField, PrimaryKeyRelatedField, SerializerMethodField
from django_filters import FilterSet, CharFilter

# REPORTE DE BENEFICIOS

class TipoReportesSerializer(ModelSerializer):
    class Meta:
        model = TipoReportes
        fields = '__all__'

class HistorialReportesSerializer(ModelSerializer):
    id_tipo_reportes = PrimaryKeyRelatedField(queryset=TipoReportes.objects.all(), write_only=True)
    id_usuario = PrimaryKeyRelatedField(queryset=AuthUser.objects.all(), write_only=True)

    tipo_reporte = CharField(source='id_tipo_reportes.nombre', read_only=True)
    codigo_usuario = CharField(source='id_usuario.dni', read_only=True)
    tipo_usuario = CharField(source='id_usuario.id_tipo_usuario.nombre', read_only=True)
    usuario = SerializerMethodField()
    
    class Meta:
        model = HistorialReportes
        fields = '__all__'
    
    def get_usuario(self, obj):
        return f"{obj.id_usuario.nombres} {obj.id_usuario.apellido_paterno} {obj.id_usuario.apellido_materno}"

class PermisosReportesSerializer(ModelSerializer):
    class Meta:
        model = PermisosReportes
        fields = '__all__'

# REPORTES

class ReporteBeneficiadosSerializer(ModelSerializer):
    class Meta:
        model = ReporteBeneficiados
        fields = '__all__'

class ReporteBeneficiadosFilter(FilterSet):
    beneficio = CharFilter(field_name='beneficio')

    class Meta:
        model = ReporteBeneficiados
        fields = '__all__'

class ReporteBeneficiadosDatosSerializer(Serializer):
    dni = CharField(max_length=8)
    nombres = CharField(max_length=50)
    apellidos = CharField(max_length=101)
    fecha_nacimiento = DateField()
    descuento = DecimalField(max_digits=10, decimal_places=2)

class ReporteBeneficiadosGrupoSerializer(Serializer):
    beneficio = CharField(max_length=20)
    grado = CharField(max_length=15)
    seccion = CharField(max_length=15)
    datos = ReporteBeneficiadosDatosSerializer(many=True)
    total = DecimalField(max_digits=10, decimal_places=2)

# REPORTE DE DEUDAS

class ReporteDeudasSerializer(ModelSerializer):
    class Meta:
        model = ReporteDeudas
        fields = '__all__'

class ReporteDeudasFilter(FilterSet):
    nombre = CharFilter(field_name='nombre')

    class Meta:
        model = ReporteDeudas
        fields = '__all__'

class ReporteDeudasDatosSerializer(Serializer):
    dni = CharField(max_length=8)
    nombres = CharField(max_length=50)
    apellidos = CharField(max_length=101)
    deuda = DecimalField(max_digits=11, decimal_places=2)

class ReporteDeudasGrupoSerializer(Serializer):
    nombre = CharField(max_length=20)
    grado = CharField(max_length=15)
    seccion = CharField(max_length=15)
    datos = ReporteDeudasDatosSerializer(many=True)
    total = DecimalField(max_digits=10, decimal_places=2)


# REPORTE DE METODO DE PAGO

class ReporteMetodoPagoSerializer(ModelSerializer):
    class Meta:
        model = ReporteMetodoPago
        fields = '__all__'

class ReporteMetodoPagoFilter(FilterSet):
    metodo = CharFilter(field_name='metodo')

    class Meta:
        model = ReporteMetodoPago
        fields = '__all__'

class ReporteMetodoPagoDatosSerializer(Serializer):
    dni = CharField(max_length=8)
    nombres = CharField(max_length=50)
    apellidos = CharField(max_length=101)
    fecha_vencimiento = DateField()
    monto = DecimalField(max_digits=10, decimal_places=2)

class ReporteMetodoPagoGrupoSerializer(Serializer):
    metodo = CharField(max_length=30)
    grado = CharField(max_length=15)
    seccion = CharField(max_length=15)
    datos = ReporteMetodoPagoDatosSerializer(many=True)
    total = DecimalField(max_digits=10, decimal_places=2)

# REPORTE DE INGRESOS

class ReporteIngresosSerializer(ModelSerializer):
    class Meta:
        model = ReporteIngresos
        fields = '__all__'

class ReporteIngresosFilter(FilterSet):
    tipo_pago = CharFilter(field_name='tipo_pago')

    class Meta:
        model = ReporteIngresos
        fields = '__all__'

class ReporteIngresosDatosSerializer(Serializer):
    dni = CharField(max_length=8)
    nombres = CharField(max_length=50)
    apellidos = CharField(max_length=101)
    fecha_pago = DateField()
    ingresos = DecimalField(max_digits=11, decimal_places=2)

class ReporteIngresosGrupoSerializer(Serializer):
    tipo_pago = CharField(max_length=20)
    mes = CharField(max_length=9)
    año = IntegerField()
    datos = ReporteIngresosDatosSerializer(many=True)
    total = DecimalField(max_digits=10, decimal_places=2)