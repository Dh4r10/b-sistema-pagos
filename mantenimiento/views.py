from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *

# Create your views here.

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset=Confirguracion.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=ConfiguracionSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=ConfiguracionFilter

class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset=Auditoria.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=AuditoriaSerializer
