from rest_framework import viewsets, permissions
from .serializers import ReporteBeneficiadosSerializer, ReporteBeneficiadosFilter, ReporteBeneficiadosDatosSerializer, ReporteBeneficiadosGrupoSerializer, ReporteDeudasSerializer, ReporteDeudasFilter, ReporteDeudasDatosSerializer, ReporteDeudasGrupoSerializer, ReporteMetodoPagoSerializer, ReporteMetodoPagoFilter, ReporteMetodoPagoDatosSerializer, ReporteMetodoPagoGrupoSerializer, ReporteIngresosSerializer, ReporteIngresosFilter, ReporteIngresosDatosSerializer, ReporteIngresosGrupoSerializer

from .models import ReporteBeneficiados, ReporteDeudas, ReporteMetodoPago, ReporteIngresos
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum

# Create your views here.

class ReporteBeneficiadosViewSet(viewsets.ModelViewSet):
    queryset = ReporteBeneficiados.objects.all()
    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
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
    
class ReporteDeudasViewSet(viewsets.ModelViewSet):
    queryset = ReporteDeudas.objects.all()
    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
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

class ReporteMetodoPagoViewSet(viewsets.ModelViewSet):
    queryset = ReporteMetodoPago.objects.all()
    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
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
    
class ReporteIngresosViewSet(viewsets.ModelViewSet):
    queryset = ReporteIngresos.objects.all()
    permission_classes = [
        # IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = ReporteIngresosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReporteIngresosFilter

    @action(detail=False, methods=['get'])
    def agrupado(self, request):
        tipo_pago = request.query_params.get('tipo_pago', None)
        
        if tipo_pago:
            filtered_queryset = ReporteIngresos.objects.filter(tipo_pago=tipo_pago).order_by('mes', 'año', 'tipo_pago')
        else:
            filtered_queryset = self.queryset.order_by('mes', 'año', 'tipo_pago')

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