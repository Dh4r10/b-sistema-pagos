from .serializers import *
from .pagination import PageNumberPagination
from .filters import AlumnoFilter
from .lists import AlumnoSerializerList
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache import cache
from utils import get_cache_key, invalidate_cache, store_cache_key

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
    serializer_class = AlumnoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AlumnoFilter
    pagination_class = PageNumberPagination
    cache_prefix = "alumnos_"  # Usar un prefijo común para toda la cache de alumnos
    cache_key_list = "alumnos_cache_keys"  # Clave para almacenar las claves de cache

    def list(self, request, *args, **kwargs):
        cache_key = get_cache_key(self, request)
        cached_response = cache.get(cache_key)
        if cached_response:
            return Response(cached_response, status=HTTP_200_OK)
        
        queryset = self.filter_queryset(self.get_queryset())

        # Prefetch related data if necessary
        queryset = queryset.select_related('id_beneficio')

        # Ordenar por nombre completo del alumno
        queryset = queryset.order_by('nombres', 'apellido_paterno', 'apellido_materno')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = AlumnoSerializerList(page, many=True)
            response_data = self.get_paginated_response(serializer.data).data
            cache.set(cache_key, response_data, timeout=60*15)  # Cache for 15 minutes
            store_cache_key(self, cache_key)  # Almacenar la clave de cache
            return Response(response_data, status=HTTP_200_OK)

        serializer = AlumnoSerializerList(queryset, many=True)
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

class InscribirAlumnoAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = InscribirAlumnoSerializer(data=request.data)

        if serializer.is_valid():
            result = serializer.save()
            return Response(result, status=HTTP_201_CREATED)
        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
