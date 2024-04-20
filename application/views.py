from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoUsuario.objects.all()
    permission_classes = [
        IsAuthenticated,
        # permissions.AllowAny,
    ]
    serializer_class = TipoUsuarioSerializer

class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    permission_classes = [
        IsAuthenticated,
        # permissions.AllowAny,
    ]
    serializer_class = AuthUserSerializer