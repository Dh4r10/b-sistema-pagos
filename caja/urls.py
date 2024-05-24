from .views import CajaViewSet, TurnoCajaViewSet, AperturaViewSet, MovimientoViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api/caja', CajaViewSet, basename='caja')
router.register('api/turno-caja', TurnoCajaViewSet, basename='turno-caja')
router.register('api/apertura', AperturaViewSet, basename='apertura')
router.register('api/movimiento', MovimientoViewSet, basename='movimiento')

urlpatterns = [
    path('', include(router.urls)),
]