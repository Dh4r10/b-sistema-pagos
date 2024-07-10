from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class BeneficioViewSet(viewsets.ModelViewSet):
    queryset = Beneficio.objects.all()
    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = BeneficioSerializer

class FamiliarViewSet(viewsets.ModelViewSet):
    queryset = Familiar.objects.all()
    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = FamiliarSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = AlumnoSerializer

class AlumnoFamiliarViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = AlumnoFamiliarSerializer

    def get_queryset(self):
        id_alumno = self.request.query_params.get('id_alumno')
        if id_alumno is not None:
            return AlumnoFamiliar.objects.filter(id_alumno=id_alumno)
        return AlumnoFamiliar.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Si necesitas devolver una respuesta JSON específica
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class EstudiantesActivosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EstudiantesActivos.objects.all()
    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = EstudiantesActivosSerializer

class EstudiantesEliminadosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EstudiantesEliminados.objects.all()
    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = EstudiantesEliminadosSerializer

class EstudiantesSolicitudEliminacionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EstudiantesSolicitudEliminacion.objects.all()
    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = EstudiantesSolicitudEliminacionSerializer
