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

class AreaMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=AreaMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=AreaMantenimientoSerializar


class MetodoPagoMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=MetodoPagoMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=MetodoPagoMantenimientoSerializar
class TipoPagoMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=TipoPagoMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=TipoPagoMantenimientoSerializar
class GradoMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=GradoMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=GradoMantenimientoSerializar
class SeccionMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=SeccionMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=SeccionMantenimientoSerializar
class ConfirmacionMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=ConfirmacionMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=ConfirmacionMantenimientoSerializar

class SexoMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=SexoMantenimiento.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=SexoMantenimientoSerializar

class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset=Auditoria.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=AuditoriaSerializar