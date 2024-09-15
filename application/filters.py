import django_filters
from .models import AuthUser
from django.db.models import Q, Value
from django.db.models.functions import Concat

class UserFilter(django_filters.FilterSet):
    is_active = django_filters.BooleanFilter(field_name='is_active')
    tipo_usuario = django_filters.CharFilter(field_name='id_tipo_usuario__nombre', lookup_expr='icontains')
    last_login = django_filters.DateTimeFilter(field_name='last_login', lookup_expr='icontains')
    buscador = django_filters.CharFilter(method='filter_buscador')

    class Meta:
        model = AuthUser
        fields = ['is_active', 'tipo_usuario', 'last_login', 'buscador']

    def filter_buscador(self, queryset, name, value):
        queryset = queryset.annotate(
            usuario=Concat('nombres', Value(' '), 'apellido_paterno', Value(' '), 'apellido_materno')
        )
        return queryset.filter(
            Q(usuario__icontains=value) |
            Q(dni__icontains=value) |
            Q(email__icontains=value) |
            Q(id_tipo_usuario__nombre__icontains=value) 
        )