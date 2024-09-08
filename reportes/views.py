from .serializers import ReporteBeneficiadosSerializer, ReporteBeneficiadosFilter, ReporteBeneficiadosDatosSerializer, ReporteBeneficiadosGrupoSerializer, ReporteDeudasSerializer, ReporteDeudasFilter, ReporteDeudasDatosSerializer, ReporteDeudasGrupoSerializer, ReporteMetodoPagoSerializer, ReporteMetodoPagoFilter, ReporteMetodoPagoDatosSerializer, ReporteMetodoPagoGrupoSerializer, ReporteIngresosSerializer, ReporteIngresosFilter, ReporteIngresosDatosSerializer, ReporteIngresosGrupoSerializer, TipoReportesSerializer, HistorialReportesSerializer, PermisosReportesSerializer
from .models import ReporteBeneficiados, ReporteDeudas, ReporteMetodoPago, ReporteIngresos, TipoReportes, HistorialReportes, PermisosReportes

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum

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
    filter_backends = (OrderingFilter,)
    ordering_fields = ['fecha']
    ordering = ['-fecha']

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