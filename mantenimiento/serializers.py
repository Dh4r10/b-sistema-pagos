from rest_framework import serializers
from .models import *
from django_filters import FilterSet

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Confirguracion
        fields= '__all__'

class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Auditoria
        fields='__all__'

# OPTIMIZACION

class ConfiguracionFilter(FilterSet):
    class Meta:
        model=Confirguracion
        fields=['tabla']