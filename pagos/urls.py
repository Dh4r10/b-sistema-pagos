from rest_framework import routers
from .views import *
from django.urls import path,include
from pagos import views

router=routers.DefaultRouter()

router.register('api/tipo-pagos',views.TipoPagoViewSet, basename='tipo_pago' )
router.register('api/cronograma-pago',views.CronogramaPagoViewSet, basename='cronograma_pago' )
router.register('api/pediente',views.PendienteViewSet, basename='pendiente' )
router.register('api/pagos',views.PagoViewSet, basename='pagos' )
router.register('api/historial-pagos',views.HistorialPagosViewSet, basename='historial-pagos' )

urlpatterns = [
    path('', include(router.urls)),
    path('api/estado-deuda',views.estado_deuda,name='estado-deuda'),
]