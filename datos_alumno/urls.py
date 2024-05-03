from rest_framework import routers
from .views import *
from django.urls import path, include
from .views import *
from datos_alumno import views

router = routers.DefaultRouter()

router.register('api/beneficio', views.BeneficioViewSet, basename='beneficio')
router.register('api/familiar', views.FamiliarViewSet, basename='familiar')
router.register('api/alumno', views.AlumnoViewSet, basename='alumno')
router.register('api/alumno_x_familiar', views.AlumnoFamiliarViewSet, basename='alumno_x_familiar')

urlpatterns = [
    path('', include(router.urls)),
]