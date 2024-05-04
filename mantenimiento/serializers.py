from rest_framework import serializers
from .models import *

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Confirguracion
        fields= '__all__'