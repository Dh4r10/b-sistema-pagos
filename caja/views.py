from .models import Caja, TurnoCaja, Apertura, Movimiento,AperturaMovimiento,HistorialPagos,AperturaCaja
from .serializers import CajaSerializer, TurnoCajaSerializer, AperturaSerializer, MovimientoSerializer,AperturaMovimientoSerializer,HistorialPagosSerializer,AperturaCajaSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from application.models import AuthUser
from django.contrib.auth.hashers import make_password

# Create your views here.

class CajaViewSet(ModelViewSet):
    queryset = Caja.objects.all()
    permission_classes = [
        #IsAuthenticated,
        AllowAny,
    ]
    serializer_class = CajaSerializer

class TurnoCajaViewSet(ModelViewSet):
    queryset = TurnoCaja.objects.all()
    permission_classes = [
        # IsAuthenticated
        AllowAny
    ]
    serializer_class = TurnoCajaSerializer

class AperturaViewSet(ModelViewSet):
    queryset = Apertura.objects.all().order_by("-id") 
    permission_classes = [
        # IsAuthenticated
        AllowAny
    ]
    serializer_class = AperturaSerializer

class MovimientoViewSet(ModelViewSet):
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

class AperturaMovimientoViewSet(ModelViewSet):
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

class HistorialPagosViewSet(ModelViewSet):
    queryset = HistorialPagos.objects.all()
    permission_classes = [
        # IsAuthenticated
        AllowAny
    ]
    serializer_class =HistorialPagosSerializer

class AperturaCajaViewSet(ModelViewSet):
    queryset = AperturaCaja.objects.all()
    permission_classes = [
        # IsAuthenticated
        AllowAny
    ]
    serializer_class =AperturaCajaSerializer
#Esto es la lógica para obtener la contraseña   
@api_view(["POST"])
def password_anulacion(request):
    password=request.data.get("password")
    print(password)
    try:
        #buscas la contrasñea del usuario
        user=AuthUser.objects.get(username=password)

        if user.id_tipo_usuario.nombre!="DIRECTOR":
            return Response({'message': 'Usuario no autorizado'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not user.is_active:
            return Response({'message': 'User is not active'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message': 'Password changed'}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

