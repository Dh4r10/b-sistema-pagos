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

class MesesMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=MesesMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=MesesMantenimientoSerializer

class MetodoPagoMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=MetodoPagoMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=MetodoPagoMantenimientoSerializer

class TipoPagoMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=TipoPagoMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=TipoPagoMantenimientoSerializer

class GradoMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=GradoMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=GradoMantenimientoSerializer

class SeccionMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=SeccionMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=SeccionMantenimientoSerializer

class AreaMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=AreaMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=AreaMantenimientoSerializer

class SexoMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=SexoMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=SexoMantenimientoSerializer