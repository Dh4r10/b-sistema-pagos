from .views import CajaViewSet, TurnoCajaViewSet, AperturaViewSet, MovimientoViewSet,AperturaMovimientoViewSet,HistorialPagosViewSet,AperturaCajaViewSet
from django.urls import path, include
from rest_framework import routers
from caja import views

router = routers.DefaultRouter()

router.register('api/caja', CajaViewSet, basename='caja')
router.register('api/turno-caja', TurnoCajaViewSet, basename='turno-caja')
router.register('api/apertura', AperturaViewSet, basename='apertura')
router.register('api/movimiento', MovimientoViewSet, basename='movimiento')
router.register('api/apertura-movimiento',AperturaMovimientoViewSet , basename='apertura-movimiento')
router.register('api/historial-pagos',HistorialPagosViewSet , basename='historial-pagos')
router.register('api/apertura-caja',AperturaCajaViewSet , basename='apertura-caja')

urlpatterns = [
    path('', include(router.urls)),
    path('api/password-anulacion',views.password_anulacion,name='password-anulacion'),
    path('api/reniec/pagos',views.ruc_Reniec,name='ruc-reniec')
]