from rest_framework import serializers
from .models import ReporteBeneficiados, ReporteDeudas, ReporteMetodoPago, ReporteIngresos
import django_filters

# REPORTE DE BENEFICIOS

class ReporteBeneficiadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteBeneficiados
        fields = '__all__'

class ReporteBeneficiadosFilter(django_filters.FilterSet):
    beneficio = django_filters.CharFilter(field_name='beneficio')

    class Meta:
        model = ReporteBeneficiados
        fields = '__all__'

class ReporteBeneficiadosDatosSerializer(serializers.Serializer):
    dni = serializers.CharField(max_length=8)
    nombres = serializers.CharField(max_length=50)
    apellidos = serializers.CharField(max_length=101)
    fecha_nacimiento = serializers.DateField()
    descuento = serializers.DecimalField(max_digits=10, decimal_places=2)

class ReporteBeneficiadosGrupoSerializer(serializers.Serializer):
    beneficio = serializers.CharField(max_length=20)
    grado = serializers.CharField(max_length=15)
    seccion = serializers.CharField(max_length=15)
    datos = ReporteBeneficiadosDatosSerializer(many=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2)

# REPORTE DE DEUDAS

class ReporteDeudasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteDeudas
        fields = '__all__'

class ReporteDeudasFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(field_name='nombre')

    class Meta:
        model = ReporteDeudas
        fields = '__all__'

class ReporteDeudasDatosSerializer(serializers.Serializer):
    dni = serializers.CharField(max_length=8)
    nombres = serializers.CharField(max_length=50)
    apellidos = serializers.CharField(max_length=101)
    deuda = serializers.DecimalField(max_digits=11, decimal_places=2)

class ReporteDeudasGrupoSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=20)
    grado = serializers.CharField(max_length=15)
    seccion = serializers.CharField(max_length=15)
    datos = ReporteDeudasDatosSerializer(many=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2)


# REPORTE DE METODO DE PAGO

class ReporteMetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteMetodoPago
        fields = '__all__'

class ReporteMetodoPagoFilter(django_filters.FilterSet):
    metodo = django_filters.CharFilter(field_name='metodo')

    class Meta:
        model = ReporteMetodoPago
        fields = '__all__'

class ReporteMetodoPagoDatosSerializer(serializers.Serializer):
    dni = serializers.CharField(max_length=8)
    nombres = serializers.CharField(max_length=50)
    apellidos = serializers.CharField(max_length=101)
    fecha_vencimiento = serializers.DateField()
    monto = serializers.DecimalField(max_digits=10, decimal_places=2)

class ReporteMetodoPagoGrupoSerializer(serializers.Serializer):
    metodo = serializers.CharField(max_length=30)
    grado = serializers.CharField(max_length=15)
    seccion = serializers.CharField(max_length=15)
    datos = ReporteMetodoPagoDatosSerializer(many=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2)

# REPORTE DE INGRESOS

class ReporteIngresosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteIngresos
        fields = '__all__'

class ReporteIngresosFilter(django_filters.FilterSet):
    tipo_pago = django_filters.CharFilter(field_name='tipo_pago')

    class Meta:
        model = ReporteIngresos
        fields = '__all__'

class ReporteIngresosDatosSerializer(serializers.Serializer):
    dni = serializers.CharField(max_length=8)
    nombres = serializers.CharField(max_length=50)
    apellidos = serializers.CharField(max_length=101)
    fecha_pago = serializers.DateField()
    ingresos = serializers.DecimalField(max_digits=11, decimal_places=2)

class ReporteIngresosGrupoSerializer(serializers.Serializer):
    tipo_pago = serializers.CharField(max_length=20)
    mes = serializers.CharField(max_length=9)
    año = serializers.IntegerField()
    datos = ReporteIngresosDatosSerializer(many=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2)