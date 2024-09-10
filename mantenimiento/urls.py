from rest_framework import routers
from .views import *
from django.urls import path,include
from mantenimiento import views

router=routers.DefaultRouter()

router.register('api/configuracion',views.ConfiguracionViewSet, basename='configuracion' )
router.register('api/auditoria',views.AuditoriaViewSet, basename='auditoria')

#Estamos incluyendo las rutas a la ruta principal de la app
urlpatterns = [
    path('', include(router.urls)),
]