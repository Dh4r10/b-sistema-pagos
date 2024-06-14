from rest_framework import serializers
from .models import Caja, TurnoCaja, Apertura, Movimiento,AperturaMovimiento,HistorialPagos,AperturaCaja

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
    fecha = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)
    class Meta:
        model = Movimiento
        fields = '__all__'

class AperturaMovimientoSerializer(serializers.ModelSerializer):
    fecha = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)
    class Meta:
        model = AperturaMovimiento
        fields="__all__"
class HistorialPagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialPagos
        fields="__all__"
class AperturaCajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AperturaCaja
        fields="__all__"