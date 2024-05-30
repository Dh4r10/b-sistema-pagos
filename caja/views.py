from .models import Caja, TurnoCaja, Apertura, Movimiento,AperturaMovimiento,HistorialPagos,AperturaCaja
from .serializers import CajaSerializer, TurnoCajaSerializer, AperturaSerializer, MovimientoSerializer,AperturaMovimientoSerializer,HistorialPagosSerializer,AperturaCajaSerializer
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
    queryset = Apertura.objects.all().order_by("-id") 
    permission_classes = [
        # IsAuthenticated
        AllowAny
    ]
    serializer_class = AperturaSerializer

class MovimientoViewSet(viewsets.ModelViewSet):
    #queryset = Movimiento.objects.all().order_by("-id")
    permission_classes = [
        # IsAuthenticated
        AllowAny
    ]
    serializer_class = MovimientoSerializer
    def get_queryset(self):
        queryset = Movimiento.objects.all()
        fecha = self.request.query_params.get('fecha', None)
        if fecha is not None:
            queryset = queryset.filter(fecha__date=fecha)
        return queryset

class AperturaMovimientoViewSet(viewsets.ModelViewSet):
    permission_classes = [
        # IsAuthenticated
        AllowAny
    ]
    serializer_class =AperturaMovimientoSerializer 
    def get_queryset(self):
        queryset = AperturaMovimiento.objects.all()
        id_apertura = self.request.query_params.get('id_apertura', None)
        if id_apertura is not None:
            queryset = queryset.filter(id_apertura=id_apertura)
        return queryset

class HistorialPagosViewSet(viewsets.ModelViewSet):
    queryset = HistorialPagos.objects.all()
    permission_classes = [
        # IsAuthenticated
        AllowAny
    ]
    serializer_class =HistorialPagosSerializer

class AperturaCajaViewSet(viewsets.ModelViewSet):
    queryset = AperturaCaja.objects.all()
    permission_classes = [
        # IsAuthenticated
        AllowAny
    ]
    serializer_class =AperturaCajaSerializer


