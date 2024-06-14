from django.shortcuts import render
from rest_framework import viewsets,permissions
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class TipoPagoViewSet(viewsets.ModelViewSet):
    queryset=TipoPago.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=TipoPagoSerializer

class CronogramaPagoViewSet(viewsets.ModelViewSet):
    queryset=CronogrmaPago.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=CronogramaPagoSerializer

class PendienteViewSet(viewsets.ModelViewSet):
    queryset=Pendiente.objects.all().order_by("-id")
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=PendienteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PendienteFilter


class PagoViewSet(viewsets.ModelViewSet):
    queryset=Pagos.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=PagosSerializer
    