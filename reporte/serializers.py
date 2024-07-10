# serializers.py
from rest_framework import serializers
from .models import ReporteMetodosPagos

class ReporteMetodosPagosSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReporteMetodosPagos
        fields = '__all__'
