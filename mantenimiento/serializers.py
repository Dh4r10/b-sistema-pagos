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

class MetodoPagoMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model=MetodoPagoMantenimiento
        fields='__all__'

class TipoPagoMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TipoPagoMantenimiento
        fields='__all__'

class GradoMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model=GradoMantenimiento
        fields='__all__'

class SeccionMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model=SeccionMantenimiento
        fields='__all__'

class AreaMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model=AreaMantenimiento
        fields='__all__'

class SexoMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model=SexoMantenimiento
        fields='__all__'