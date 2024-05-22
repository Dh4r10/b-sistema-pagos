from rest_framework import serializers
from .models import *
from datos_alumno .models import *
from datos_alumno .serializers import *

class TipoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model= TipoPago
        fields='__all__'

class CronogramaPagoSerializer(serializers.ModelSerializer):
    id_tipo_pago=serializers.PrimaryKeyRelatedField(queryset=TipoPago.objects.all(), write_only=True)
    tipo_pago= TipoPagoSerializer(source="id_tipo_pago",read_only=True)

    class Meta:
        model=CronogrmaPago
        fields="__all__"

class PendienteSerializer(serializers.ModelSerializer):
    id_alumno=serializers.PrimaryKeyRelatedField(queryset=Alumno.objects.all(),write_only=True)
    alumno=AlumnoSerializer(source="id_alumno",read_only=True)
    id_crnograma_pago=serializers.PrimaryKeyRelatedField(queryset=CronogrmaPago.objects.all(),write_only=True)
    crnograma_pago=CronogramaPagoSerializer(source="id_cronograma_pago",read_only=True)

    class Meta:
        model=Pendiente
        fields="__all__"

class PagosSerializer(serializers.ModelSerializer):
    id_pendiente=serializers.PrimaryKeyRelatedField(queryset=Pendiente.objects.all(),write_only=True)
    pendiente=PendienteSerializer(source="id_pendiente",read_only=True)

    class Meta:
        model=Pagos
        fields="__all__"
