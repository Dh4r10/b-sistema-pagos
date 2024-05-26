from rest_framework import serializers
from .models import Caja, TurnoCaja, Apertura, Movimiento

class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = '__all__'

class TurnoCajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurnoCaja
        fields = '__all__'

class AperturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apertura
        fields = '__all__'

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = '__all__'