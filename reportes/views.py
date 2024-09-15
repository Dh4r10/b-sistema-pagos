from .serializers import ReporteBeneficiadosSerializer, ReporteBeneficiadosFilter, ReporteBeneficiadosDatosSerializer, ReporteBeneficiadosGrupoSerializer, ReporteDeudasSerializer, ReporteDeudasFilter, ReporteDeudasDatosSerializer, ReporteDeudasGrupoSerializer, ReporteMetodoPagoSerializer, ReporteMetodoPagoFilter, ReporteMetodoPagoDatosSerializer, ReporteMetodoPagoGrupoSerializer, ReporteIngresosSerializer, ReporteIngresosFilter, ReporteIngresosDatosSerializer, ReporteIngresosGrupoSerializer, TipoReportesSerializer, HistorialReportesSerializer, PermisosReportesSerializer
from .models import ReporteBeneficiados, ReporteDeudas, ReporteMetodoPago, ReporteIngresos, TipoReportes, HistorialReportes, PermisosReportes
from .pagination import PageNumberPagination
from .lists import HistorialReportesSerializerList

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.status import HTTP_200_OK
from django.db import connection

from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from django.core.cache import cache

from utils import get_cache_key, store_cache_key, invalidate_cache

# Create your views here.

class TipoReportesViewSet(ModelViewSet):
    queryset = TipoReportes.objects.all()
    permission_classes = [
        AllowAny
    ]
    serializer_class = TipoReportesSerializer

class HistorialReportesViewSet(ModelViewSet):
    queryset = HistorialReportes.objects.all()
    permission_classes = [
        AllowAny
    ]
    serializer_class = HistorialReportesSerializer
    pagination_class = PageNumberPagination
    cache_prefix = "historialreportes_"  # Usar un prefijo común para toda la cache de historial de reportes
    cache_key_list = "historialreportes_cache_keys"  # Clave para almacenar las claves de cache
    
    def list(self, request):
        cache_key = get_cache_key(self, request)
        cached_response = cache.get(cache_key)
        if cached_response:
            return Response(cached_response, status=HTTP_200_OK)
        
        # Obtener los parámetros de la solicitud GET
        tipo_usuario = request.query_params.get('tipo_usuario')
        tipo_reporte = request.query_params.get('tipo_reporte')
        fecha = request.query_params.get('fecha')
        buscador = request.query_params.get('buscador')

        if buscador is not None:
            buscador = '%' + buscador.upper() + '%'

        with connection.cursor() as cursor:
            # Llamar al procedimiento almacenado
            cursor.callproc('getAllReportHistory', [tipo_usuario, tipo_reporte, fecha, buscador])

            keys = ['id', 'dni', 'usuario', 'tipo_usuario', 'tipo_reporte', 'descripcion', 'fecha']

            # Si el procedimiento devuelve resultados
            results = cursor.fetchall()

            data = [dict(zip(keys, row)) for row in results]

        page = self.paginate_queryset(data)
        if page is not None:
            serializer = HistorialReportesSerializerList(page, many=True)
            response_data = self.get_paginated_response(serializer.data).data
            cache.set(cache_key, response_data, timeout=60*15)  # Cache for 15 minutes
            store_cache_key(self, cache_key)  # Almacenar la clave de cache
            return Response(response_data, status=HTTP_200_OK)

        serializer = HistorialReportesSerializerList(data, many=True)
        response_data = serializer.data
        cache.set(cache_key, response_data, timeout=60*15)  # Cache for 15 minutes
        store_cache_key(self, cache_key)  # Almacenar la clave de cache
        return Response(response_data, status=HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            invalidate_cache(self)  # Invalida la cache si la operación fue exitosa
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code in [200, 204]:
            invalidate_cache(self)  # Invalida la cache si la operación fue exitosa
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        if response.status_code in [200, 204]:
            invalidate_cache(self)  # Invalida la cache si la operación fue exitosa
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == 204:
            invalidate_cache(self)  # Invalida la cache si la operación fue exitosa
        return response

class PermisosReportesViewSet(ModelViewSet):
    queryset = PermisosReportes.objects.all()
    permission_classes = [
        AllowAny
    ]
    serializer_class = PermisosReportesSerializer

# REPORTES

class ReporteBeneficiadosViewSet(ModelViewSet):
    queryset = ReporteBeneficiados.objects.all()
    permission_classes = [
        # IsAuthenticated,
        AllowAny,
    ]
    serializer_class = ReporteBeneficiadosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReporteBeneficiadosFilter

    @action(detail=False, methods=['get'])
    def agrupado(self, request):
        beneficio = request.query_params.get('beneficio', None)
        
        if beneficio:
            filtered_queryset = ReporteBeneficiados.objects.filter(beneficio=beneficio).order_by('grado', 'seccion', 'beneficio')
        else:
            filtered_queryset = self.queryset.order_by('grado', 'seccion', 'beneficio')

        # Agrupar por beneficio, grado y sección, y sumar los descuentos
        agrupados = filtered_queryset.values('beneficio', 'grado', 'seccion').annotate(total=Sum('descuento'))
        resultado = []

        for grupo in agrupados:
            beneficio = grupo['beneficio']
            grado = grupo['grado']
            seccion = grupo['seccion']
            total = grupo['total']

            # Obtener los datos individuales para cada grupo
            datos = filtered_queryset.filter(beneficio=beneficio, grado=grado, seccion=seccion)
            datos_serializados = ReporteBeneficiadosDatosSerializer(datos, many=True).data

            # Construir el resultado final para cada grupo
            resultado.append({
                'beneficio': beneficio,
                'grado': grado,
                'seccion': seccion,
                'datos': datos_serializados,
                'total': total
            })

        # Serializar el resultado final
        serializer = ReporteBeneficiadosGrupoSerializer(resultado, many=True)
        return Response(serializer.data)
    
class ReporteDeudasViewSet(ModelViewSet):
    queryset = ReporteDeudas.objects.all()
    permission_classes = [
        # IsAuthenticated,
        AllowAny,
    ]
    serializer_class = ReporteDeudasSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReporteDeudasFilter

    @action(detail=False, methods=['get'])
    def agrupado(self, request):
        nombre = request.query_params.get('nombre', None)
        
        if nombre:
            filtered_queryset = ReporteDeudas.objects.filter(nombre=nombre).order_by('grado', 'seccion', 'nombre')
        else:
            filtered_queryset = self.queryset.order_by('grado', 'seccion', 'nombre')

        # Agrupar por beneficio, grado y sección, y sumar los descuentos
        agrupados = filtered_queryset.values('nombre', 'grado', 'seccion').annotate(total=Sum('deuda'))
        resultado = []

        for grupo in agrupados:
            nombre = grupo['nombre']
            grado = grupo['grado']
            seccion = grupo['seccion']
            total = grupo['total']

            # Obtener los datos individuales para cada grupo
            datos = filtered_queryset.filter(nombre=nombre, grado=grado, seccion=seccion)
            datos_serializados = ReporteDeudasDatosSerializer(datos, many=True).data

            # Construir el resultado final para cada grupo
            resultado.append({
                'nombre': nombre,
                'grado': grado,
                'seccion': seccion,
                'datos': datos_serializados,
                'total': total
            })

        # Serializar el resultado final
        serializer = ReporteDeudasGrupoSerializer(resultado, many=True)
        return Response(serializer.data)

class ReporteMetodoPagoViewSet(ModelViewSet):
    queryset = ReporteMetodoPago.objects.all()
    permission_classes = [
        # IsAuthenticated,
        AllowAny,
    ]
    serializer_class = ReporteMetodoPagoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReporteMetodoPagoFilter

    @action(detail=False, methods=['get'])
    def agrupado(self, request):
        metodo = request.query_params.get('metodo', None)
        
        if metodo:
            filtered_queryset = ReporteMetodoPago.objects.filter(metodo=metodo).order_by('grado', 'seccion', 'metodo')
        else:
            filtered_queryset = self.queryset.order_by('grado', 'seccion', 'metodo')

        # Agrupar por beneficio, grado y sección, y sumar los descuentos
        agrupados = filtered_queryset.values('metodo', 'grado', 'seccion').annotate(total=Sum('monto'))
        resultado = []

        for grupo in agrupados:
            metodo = grupo['metodo']
            grado = grupo['grado']
            seccion = grupo['seccion']
            total = grupo['total']

            # Obtener los datos individuales para cada grupo
            datos = filtered_queryset.filter(metodo=metodo, grado=grado, seccion=seccion)
            datos_serializados = ReporteMetodoPagoDatosSerializer(datos, many=True).data

            # Construir el resultado final para cada grupo
            resultado.append({
                'metodo': metodo,
                'grado': grado,
                'seccion': seccion,
                'datos': datos_serializados,
                'total': total
            })

        # Serializar el resultado final
        serializer = ReporteMetodoPagoGrupoSerializer(resultado, many=True)
        return Response(serializer.data)
    
class ReporteIngresosViewSet(ModelViewSet):
    queryset = ReporteIngresos.objects.all()
    permission_classes = [
        # IsAuthenticated,
        AllowAny,
    ]
    serializer_class = ReporteIngresosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReporteIngresosFilter

    @action(detail=False, methods=['get'])
    def agrupado(self, request):
        tipo_pago = request.query_params.get('tipo_pago', None)
        fecha_inicial = request.query_params.get('fecha_inicial', None)
        fecha_final = request.query_params.get('fecha_final', None)
        
        # if tipo_pago:
            
        #     if (fecha_inicial and fecha_final):
        #         filtered_queryset = ReporteIngresos.objects.filter(tipo_pago=tipo_pago, fecha_pago__range=[fecha_inicial, fecha_final]).order_by('mes', 'año', 'tipo_pago', '-fecha_pago')
            
        #     else:
        #         filtered_queryset = ReporteIngresos.objects.filter(tipo_pago=tipo_pago).order_by('mes', 'año', 'tipo_pago', '-fecha_pago')

        # else:
        #     filtered_queryset = self.queryset.order_by('mes', 'año', 'tipo_pago', '-fecha_pago')

        if tipo_pago and not (fecha_inicial and fecha_final):
            filtered_queryset = ReporteIngresos.objects.filter(tipo_pago=tipo_pago).order_by('mes', 'año', 'tipo_pago', '-fecha_pago')
        elif tipo_pago and (fecha_inicial and fecha_final):
            filtered_queryset = ReporteIngresos.objects.filter(tipo_pago=tipo_pago, fecha_pago__range=[fecha_inicial, fecha_final]).order_by('mes', 'año', 'tipo_pago', '-fecha_pago')
        elif not tipo_pago and (fecha_inicial and fecha_final):
            filtered_queryset = ReporteIngresos.objects.filter(fecha_pago__range=[fecha_inicial, fecha_final]).order_by('mes', 'año', 'tipo_pago', '-fecha_pago')
        else:
            filtered_queryset = self.queryset.order_by('mes', 'año', 'tipo_pago', '-fecha_pago')

        # Agrupar por beneficio, grado y sección, y sumar los descuentos
        agrupados = filtered_queryset.values('mes', 'año', 'tipo_pago').annotate(total=Sum('ingresos'))
        resultado = []

        for grupo in agrupados:
            tipo_pago = grupo['tipo_pago']
            mes = grupo['mes']
            año = grupo['año']
            total = grupo['total']

            # Obtener los datos individuales para cada grupo
            datos = filtered_queryset.filter(tipo_pago=tipo_pago, mes=mes, año=año)
            datos_serializados = ReporteIngresosDatosSerializer(datos, many=True).data

            # Construir el resultado final para cada grupo
            resultado.append({
                'tipo_pago': tipo_pago,
                'mes': mes,
                'año': año,
                'datos': datos_serializados,
                'total': total
            })

        # Serializar el resultado final
        serializer = ReporteIngresosGrupoSerializer(resultado, many=True)
        return Response(serializer.data)