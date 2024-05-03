from rest_framework import viewsets, permissions
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