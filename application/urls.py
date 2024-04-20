from rest_framework import routers
from .views import *
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
from application import views

router = routers.DefaultRouter()
router.register('api/tipo_usuario', views.TipoUsuarioViewSet, basename='tipo_usuario')
router.register('api/usuario', views.AuthUserViewSet, basename='usuario')
router.register('api/modulos', views.ModulosViewSet, basename='modulos')
router.register('api/permisos', views.PermisosViewSet, basename='permisos')
router.register('api/usuarios_activos', views.UsuariosActivosViewSet, basename='usuarios_activos')

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]