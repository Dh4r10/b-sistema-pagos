from django.shortcuts import render
from rest_framework import viewsets,permissions
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from application.models import AuthUser
from datetime import datetime
from datos_alumno.models import Alumno

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
    queryset=Pendiente.objects.filter(estado=True).order_by("-id")
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
    

@api_view(["POST"])
def estado_deuda(request):
     id_alumno=request.data.get('id')
     now=datetime.now()

     try:
         alumno=Alumno.objects.get(id=id_alumno)
         print(alumno.nombres,alumno.deuda)
         
         #Estoy sacando todos los pendientes del los alumnos aquí
         pendientes=Pendiente.objects.filter(id_alumno=id_alumno).order_by('id')

  
         primer_pendiente_false=None
         for pendiente in pendientes:
          if not pendiente.estado:
               primer_pendiente_false=pendiente
               break
         
         if(primer_pendiente_false !=None):
             if primer_pendiente_false.id_cronograma_pago.fecha_fin<now.date():
                (primer_pendiente_false.id_cronograma_pago.fecha_fin,now.date())
                alumno.deuda=True
                alumno.save()       
    

          #Aquí sacamos el primer pendiente con el estado 1, osea con deudas
         primer_pendiente_true=None
         for pendiente in pendientes:
            if pendiente.estado:
                primer_pendiente_true = pendiente 
                break
              
         #Si la fecha actua de menor que la del primero 1, entonces es deudas 
         if(primer_pendiente_true!=None):  
             if primer_pendiente_true.id_cronograma_pago.fecha_inicio < now.date():
              print(now.date(),primer_pendiente_true.id_cronograma_pago.fecha_inicio)   
              alumno.deuda=False
              alumno.save()

         return Response({'message': 'Estado de deuda actualizado'},status=status.HTTP_200_OK)

     except Exception as e:
        return Response({str(e)}, status=status.HTTP_400_BAD_REQUEST) 
class HistorialPagosViewSet(viewsets.ModelViewSet):
    queryset=HistorialPagos.objects.all()
    permission_classes=[
        permissions.AllowAny,
    ]
    serializer_class=HistorialPagosSerializer