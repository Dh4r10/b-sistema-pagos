from rest_framework import routers
from .views import *
from django.urls import path,include
from mantenimiento import views

router=routers.DefaultRouter()

router.register('api/configuracion',views.ConfiguracionViewSet, basename='configuracion' )
router.register('api/meses_mantenimiento',views.MesesManteniminetoViewSet, basename='meses_mantenimiento')
router.register('api/area_mantenimiento',views.AreaMantenimientoViewSet, basename='area_mantenimiento')

router.register('api/metodo-pago_mantenimiento',views.MetodoPagoMantenimientoViewSet, basename='metodo_pago')
router.register('api/tipo-pago_mantenimiento',views.TipoPagoMantenimientoViewSet, basename='tipo_pago')
router.register('api/grado_mantenimiento',views.GradoMantenimientoViewSet, basename='grado')
router.register('api/seccion_mantenimiento',views.SeccionMantenimientoViewSet, basename='seccion')
router.register('api/confirmacion_mantenimiento',views.ConfirmacionMantenimientoViewSet, basename='confirmacion')
router.register('api/sexo_mantenimiento',views.SexoMantenimientoViewSet, basename='sexo')

#Tabla Auditoria
router.register('api/auditoria',views.AuditoriaViewSet, basename='auditoria')

#Estamos incluyendo las rutas a la ruta principal de la app
urlpatterns = [
    path('', include(router.urls)),
]