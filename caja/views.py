from .models import Caja, TurnoCaja, Apertura, Movimiento
from .serializers import CajaSerializer, TurnoCajaSerializer, AperturaSerializer, MovimientoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

class CajaViewSet(viewsets.ModelViewSet):
    queryset = Caja.objects.all()
    permission_classes = [
        #IsAuthenticated,
        AllowAny,
    ]
    serializer_class = CajaSerializer

class TurnoCajaViewSet(viewsets.ModelViewSet):
    queryset = TurnoCaja.objects.all()
    permission_classes = [
        # IsAuthenticated
        AllowAny
    ]
    serializer_class = TurnoCajaSerializer

class AperturaViewSet(viewsets.ModelViewSet):
    queryset = Apertura.objects.all()
    permission_classes = [
        # IsAuthenticated
        AllowAny
    ]
    serializer_class = AperturaSerializer

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    permission_classes = [
        # IsAuthenticated
        AllowAny
    ]
    serializer_class = MovimientoSerializer