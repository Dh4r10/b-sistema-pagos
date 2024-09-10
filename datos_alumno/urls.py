from rest_framework import routers
from .views import BeneficioViewSet, FamiliarViewSet, AlumnoViewSet, AlumnoFamiliarViewSet, InscribirAlumnoAPIView
from django.urls import path, include


router = routers.DefaultRouter()

router.register('api/beneficio', BeneficioViewSet, basename='beneficio')
router.register('api/familiar', FamiliarViewSet, basename='familiar')
router.register('api/alumno', AlumnoViewSet, basename='alumno')
router.register('api/alumno_x_familiar', AlumnoFamiliarViewSet, basename='alumno_x_familiar')

urlpatterns = [
    path('', include(router.urls)),
    path('inscribir-alumno/', InscribirAlumnoAPIView.as_view(), name='inscribir-alumno')
]
