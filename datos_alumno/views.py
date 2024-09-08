from .serializers import *
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
import json


# Create your views here.
class BeneficioViewSet(ModelViewSet):
    queryset = Beneficio.objects.all()
    permission_classes = [
        # IsAuthenticated,
        AllowAny,
    ]
    serializer_class = BeneficioSerializer

class FamiliarViewSet(ModelViewSet):
    queryset = Familiar.objects.all()
    permission_classes = [
        # IsAuthenticated,
        AllowAny,
    ]
    serializer_class = FamiliarSerializer

class AlumnoViewSet(ModelViewSet):
    queryset = Alumno.objects.all()
    permission_classes = [
        # IsAuthenticated,
        AllowAny,
    ]
    serializer_class = AlumnoSerializer

class AlumnoFamiliarViewSet(ModelViewSet):
    permission_classes = [
        AllowAny,
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

class EstudiantesActivosViewSet(ReadOnlyModelViewSet):
    queryset = EstudiantesActivos.objects.all()
    permission_classes = [
        # IsAuthenticated,
        AllowAny,
    ]
    serializer_class = EstudiantesActivosSerializer

class EstudiantesEliminadosViewSet(ReadOnlyModelViewSet):
    queryset = EstudiantesEliminados.objects.all()
    permission_classes = [
        # IsAuthenticated,
        AllowAny,
    ]
    serializer_class = EstudiantesEliminadosSerializer

class EstudiantesSolicitudEliminacionViewSet(ReadOnlyModelViewSet):
    queryset = EstudiantesSolicitudEliminacion.objects.all()
    permission_classes = [
        # IsAuthenticated,
        AllowAny,
    ]
    serializer_class = EstudiantesSolicitudEliminacionSerializer

class InscribirAlumnoAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = InscribirAlumnoSerializer(data=request.data)

        if serializer.is_valid():
            result = serializer.save()
            return Response(result, status=HTTP_201_CREATED)
        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

  