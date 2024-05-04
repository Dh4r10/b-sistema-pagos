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