from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

# Create your views here.

class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoUsuario.objects.all()
    permission_classes = [
        #IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = TipoUsuarioSerializer

class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = AuthUserSerializer

class PermisosViewSet(viewsets.ModelViewSet):
    queryset = Permisos.objects.all()
    permission_classes = [
        #IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = PermisosSerializer

class ModulosViewSet(viewsets.ModelViewSet):
    queryset = Modulos.objects.all()
    permission_classes = [
        #IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = ModulosSerializer