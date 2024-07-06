from rest_framework import viewsets, permissions, views
from .serializers import *
from rest_framework.permissions import IsAuthenticated

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
    queryset = AlumnoFamiliar.objects.all()
    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = AlumnoFamiliarSerializer

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

class InscribirAlumnoAPIView(views.APIView):
    def post(self, request, *args, **kwargs):

        alumno = request.data.get('alumno')

        def saveAlumno(alumno):
            serializer = AlumnoSerializer(data=alumno)
            if serializer.is_valid():
                save_data = serializer.save()
                return save_data.id
            
        def saveFamiliar(familiar):
            serializer = FamiliarSerializer(data=familiar)
            if serializer.is_valid():
                save_data = serializer.save()
                return save_data.id
            
        def saveAlumnoFamiliar(relacion):
            serializer = AlumnoFamiliarSerializer(data=relacion)
            if serializer.is_valid():
                serializer.save()
                return "Relación exitosa"
            
        alumno_id = saveAlumno(alumno)
        


        