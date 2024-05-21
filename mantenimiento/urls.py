from rest_framework import routers
from .views import *
from django.urls import path,include
from mantenimiento import views

router=routers.DefaultRouter()

router.register('api/configuracion',views.ConfiguracionViewSet, basename='configuracion' )
router.register('api/meses_mantenimiento',views.MesesMantenimientoViewSet, basename='meses_mantenimiento')
router.register('api/metodo_pago_mantenimiento',views.MetodoPagoMantenimientoViewSet, basename='metodo_pago_mantenimiento')
router.register('api/tipo_pago_mantenimiento',views.TipoPagoMantenimientoViewSet, basename='tipo_pago_mantenimiento')
router.register('api/grado_mantenimiento',views.GradoMantenimientoViewSet, basename='grado_mantenimiento')
router.register('api/seccion_mantenimiento',views.SeccionMantenimientoViewSet, basename='seccion_mantenimiento')
router.register('api/area_mantenimiento',views.AreaMantenimientoViewSet, basename='area_mantenimiento')
router.register('api/sexo_mantenimiento',views.SexoMantenimientoViewSet, basename='sexo_mantenimiento')

#Estamos incluyendo las rutas a la ruta principal de la app
urlpatterns = [
    path('', include(router.urls)),
]