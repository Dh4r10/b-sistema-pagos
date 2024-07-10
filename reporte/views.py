from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ReporteMetodoPagosViewset(viewsets.ModelViewSet):
    queryset = ReporteMetodosPagos.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ReporteMetodosPagosSerializers
