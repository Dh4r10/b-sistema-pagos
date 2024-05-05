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