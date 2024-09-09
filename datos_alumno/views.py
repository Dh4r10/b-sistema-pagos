from .serializers import *
from .pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from django.db import connection


# Create your views here.
class BeneficioViewSet(ModelViewSet):
    queryset = Beneficio.objects.all()
    permission_classes = [
        # IsAuthenticated,
        AllowAny,
    ]
    serializer_class = BeneficioSerializer

class FamiliarViewSet(ModelViewSet):
    queryset = Familiar.objects.all()
    permission_classes = [
        # IsAuthenticated,
        AllowAny,
    ]
    serializer_class = FamiliarSerializer

class AlumnoViewSet(ModelViewSet):
    queryset = Alumno.objects.all()
    permission_classes = [
        # IsAuthenticated,
        AllowAny,
    ]
    serializer_class = AlumnoSerializer
    pagination_class = PageNumberPagination

    def list(self, request):
        # Obtener los parámetros de la solicitud GET
        estado = request.query_params.get('estado')
        deuda = request.query_params.get('deuda')
        eliminacion_pendiente = request.query_params.get('eliminacion_pendiente')
        beneficio = request.query_params.get('beneficio')
        turno = request.query_params.get('turno')
        grado = request.query_params.get('grado')
        seccion = request.query_params.get('seccion')
        buscador = request.query_params.get('buscador')

        if estado is not None:
            estado = True if estado.lower() == 'true' else False

        if deuda is not None:
            deuda = True if deuda.lower() == 'true' else False
        
        if eliminacion_pendiente is not None:
            eliminacion_pendiente = True if eliminacion_pendiente.lower() == 'true' else False

        if buscador is not None:
            buscador = '%' + buscador.upper() + '%'

        with connection.cursor() as cursor:
            # Llamar al procedimiento almacenado
            cursor.callproc('getAllStudents', [estado, deuda, eliminacion_pendiente, beneficio, turno, grado, seccion, buscador])

            keys = ['id', 'dni', 'alumno', 'beneficio', 'turno', 'grado', 'seccion', 'deuda']

            # Si el procedimiento devuelve resultados
            results = cursor.fetchall()

            data = [dict(zip(keys, row)) for row in results]

        # Devolver la respuesta con los resultados
        page = self.paginate_queryset(data)
        if page is not None:
            return self.get_paginated_response(page)

        # Devolver la respuesta con los resultados
        return Response(data=data, status=HTTP_200_OK)

class AlumnoFamiliarViewSet(ModelViewSet):
    permission_classes = [
        AllowAny,
    ]
    serializer_class = AlumnoFamiliarSerializer

    def get_queryset(self):
        id_alumno = self.request.query_params.get('id_alumno')
        if id_alumno is not None:
            return AlumnoFamiliar.objects.filter(id_alumno=id_alumno)
        return AlumnoFamiliar.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Si necesitas devolver una respuesta JSON específica
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class EstudiantesSolicitudEliminacionViewSet(ReadOnlyModelViewSet):
    queryset = EstudiantesSolicitudEliminacion.objects.all()
    permission_classes = [
        # IsAuthenticated,
        AllowAny,
    ]
    serializer_class = EstudiantesSolicitudEliminacionSerializer

class InscribirAlumnoAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = InscribirAlumnoSerializer(data=request.data)

        if serializer.is_valid():
            result = serializer.save()
            return Response(result, status=HTTP_201_CREATED)
        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

  