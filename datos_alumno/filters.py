import django_filters
from .models import Alumno
from django.db.models import Q, Value
from django.db.models.functions import Concat

class AlumnoFilter(django_filters.FilterSet):
    estado = django_filters.BooleanFilter(field_name='estado')
    deuda = django_filters.BooleanFilter(field_name='deuda')
    eliminacion_pendiente = django_filters.BooleanFilter(field_name='eliminacion_pendiente')
    beneficio = django_filters.CharFilter(field_name='id_beneficio__nombre', lookup_expr='icontains')
    turno = django_filters.CharFilter(field_name='turno', lookup_expr='icontains')
    grado = django_filters.CharFilter(field_name='grado', lookup_expr='icontains')
    seccion = django_filters.CharFilter(field_name='seccion', lookup_expr='icontains')
    buscador = django_filters.CharFilter(method='filter_buscador')

    class Meta:
        model = Alumno
        fields = ['estado', 'deuda', 'eliminacion_pendiente', 'beneficio', 'turno', 'grado', 'seccion', 'buscador']

    def filter_buscador(self, queryset, name, value):
        queryset = queryset.annotate(
            alumno=Concat('nombres', Value(' '), 'apellido_paterno', Value(' '), 'apellido_materno')
        )
        return queryset.filter(
            Q(dni__icontains=value) |
            Q(alumno__icontains=value) |
            Q(id_beneficio__nombre__icontains=value)
        )