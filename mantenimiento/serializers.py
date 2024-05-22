from rest_framework import serializers
from .models import *

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Confirguracion
        fields= '__all__'

class MesesMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model=MesesMantenimiento
        fields='__all__'
class AreaMantenimientoSerializar(serializers.ModelSerializer):
    class Meta:
        model=AreaMantenimiento
        fields='__all__'



class MetodoPagoMantenimientoSerializar(serializers.ModelSerializer):
    class Meta:
        model=MetodoPagoMantenimiento
        fields='__all__'

class TipoPagoMantenimientoSerializar(serializers.ModelSerializer):
    class Meta:
        model=TipoPagoMantenimiento
        fields='__all__'

class GradoMantenimientoSerializar(serializers.ModelSerializer):
    class Meta:
        model=GradoMantenimiento
        fields='__all__'

class SeccionMantenimientoSerializar(serializers.ModelSerializer):
    class Meta:
        model=SeccionMantenimiento
        fields='__all__'

class ConfirmacionMantenimientoSerializar(serializers.ModelSerializer):
    class Meta:
        model=ConfirmacionMantenimiento
        fields='__all__'

class SexoMantenimientoSerializar(serializers.ModelSerializer):
    class Meta:
        model=SexoMantenimiento
        fields='__all__'

class AuditoriaSerializar(serializers.ModelSerializer):
    class Meta:
        model=Auditoria
        fields='__all__'
