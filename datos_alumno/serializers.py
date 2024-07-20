from rest_framework.serializers import ModelSerializer, Serializer, PrimaryKeyRelatedField
from .models import *

class BeneficioSerializer(ModelSerializer):
    class Meta:
        model = Beneficio
        fields = '__all__'

class FamiliarSerializer(ModelSerializer):
    class Meta:
        model = Familiar
        fields = '__all__'

class AlumnoSerializer(ModelSerializer):
    id_beneficio = PrimaryKeyRelatedField(queryset=Beneficio.objects.all(), write_only=True)
    beneficio = BeneficioSerializer(source='id_beneficio', read_only=True)

    class Meta:
        model=Alumno
        fields='__all__'

class AlumnoFamiliarSerializer(ModelSerializer):
    id_alumno = PrimaryKeyRelatedField(queryset=Alumno.objects.all(), write_only=True)
    alumno = AlumnoSerializer(source='id_alumno', read_only=True)
    id_familiar = PrimaryKeyRelatedField(queryset=Familiar.objects.all(), write_only=True)
    familiar = FamiliarSerializer(source='id_familiar', read_only=True)

    class Meta:
        model=AlumnoFamiliar
        fields='__all__'

# SERIALIZER PERSONALIZADOS

class InscribirAlumnoSerializer(Serializer):
    alumno = AlumnoSerializer()
    familiares = FamiliarSerializer(many=True)

    def create(self, validated_data):
        alumno_data = validated_data.pop('alumno')
        familiares_data = validated_data.pop('familiares')

        alumno = Alumno.objects.create(**alumno_data)
        familiares = [
            Familiar.objects.create(**familiar_data) for familiar_data in familiares_data
        ]

        for familiar in familiares:
            AlumnoFamiliar.objects.create(id_alumno=alumno,id_familiar=familiar)

        return {'response': 'alumno creado exitosamente'}

# VISTAS

class EstudiantesActivosSerializer(ModelSerializer):
    class Meta:
        model=EstudiantesActivos
        fields= '__all__'

class EstudiantesEliminadosSerializer(ModelSerializer):
    class Meta:
        model=EstudiantesEliminados
        fields= '__all__'

class EstudiantesSolicitudEliminacionSerializer(ModelSerializer):
    class Meta:
        model=EstudiantesSolicitudEliminacion
        fields= '__all__'
