# urls.py
from rest_framework import routers
from django.urls import path, include
from .views import ReporteMetodoPagosViewset

router = routers.DefaultRouter()
router.register('api/reporte-metodo-pagos', ReporteMetodoPagosViewset, basename='reporte_metodo_pago')

urlpatterns = [
    path('', include(router.urls)),
]
