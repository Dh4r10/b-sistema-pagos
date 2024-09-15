from rest_framework import serializers
from .models import Alumno

class AlumnoSerializerList(serializers.ModelSerializer):
    alumno = serializers.SerializerMethodField()
    beneficio = serializers.SerializerMethodField()

    class Meta:
        model = Alumno
        fields = ['id', 'dni', 'alumno', 'beneficio', 'turno', 'grado', 'seccion', 'deuda']

    def get_alumno(self, obj):
        return f"{obj.nombres} {obj.apellido_paterno} {obj.apellido_materno}"

    def get_beneficio(self, obj):
        return obj.id_beneficio.nombre if obj.id_beneficio else None