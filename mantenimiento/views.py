from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
# Create your views here.
class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset=Confirguracion.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=ConfiguracionSerializer

class MesesManteniminetoViewSet(viewsets.ModelViewSet):
    queryset=MesesMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=MesesMantenimientoSerializer
class AreaMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=AreaMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=AreaMantenimientoSerializar