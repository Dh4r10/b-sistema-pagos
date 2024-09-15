from rest_framework import serializers
from .models import HistorialReportes

class HistorialReportesSerializerList(serializers.Serializer):  # Cambiamos de ModelSerializer a Serializer
    id = serializers.SerializerMethodField()
    dni = serializers.SerializerMethodField()
    usuario = serializers.SerializerMethodField()
    tipo_usuario = serializers.SerializerMethodField()
    tipo_reporte = serializers.SerializerMethodField()
    descripcion = serializers.CharField()
    fecha = serializers.DateTimeField()

    class Meta:
        fields = ['id', 'dni', 'usuario', 'tipo_usuario', 'tipo_reporte', 'descripcion', 'fecha']

    def get_id(self, obj):
        # 'obj' es un diccionario, así que accedemos como a un diccionario
        return obj.get('id')

    def get_dni(self, obj):
        return obj.get('dni')

    def get_usuario(self, obj):
        return obj.get('usuario')

    def get_tipo_usuario(self, obj):
        return obj.get('tipo_usuario')

    def get_tipo_reporte(self, obj):
        return obj.get('tipo_reporte')
