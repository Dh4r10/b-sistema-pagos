from rest_framework import serializers
from .models import *

class BeneficioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficio
        fields = '__all__'

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    id_beneficio = serializers.PrimaryKeyRelatedField(queryset=Beneficio.objects.all(), write_only=True)
    beneficio = BeneficioSerializer(source='id_beneficio', read_only=True)

    class Meta:
        model=Alumno
        fields='__all__'

class AlumnoFamiliarSerializer(serializers.ModelSerializer):
    id_alumno = serializers.PrimaryKeyRelatedField(queryset=Alumno.objects.all(), write_only=True)
    alumno = AlumnoSerializer(source='id_alumno', read_only=True)
    id_familiar = serializers.PrimaryKeyRelatedField(queryset=Familiar.objects.all(), write_only=True)
    familiar = FamiliarSerializer(source='id_familiar', read_only=True)

    class Meta:
        model=AlumnoFamiliar
        fields='__all__'

class EstudiantesActivosSerializer(serializers.ModelSerializer):
    class Meta:
        model=EstudiantesActivos
        fields= '__all__'

class EstudiantesEliminadosSerializer(serializers.ModelSerializer):
    class Meta:
        model=EstudiantesEliminados
        fields= '__all__'

class EstudiantesSolicitudEliminacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=EstudiantesSolicitudEliminacion
        fields= '__all__'
