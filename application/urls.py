from .views import TipoUsuarioViewSet, AuthUserViewSet, ModulosViewSet, PermisosViewSet, LogoutView, UpdateProfilePictureView
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from application import views

router = routers.DefaultRouter()

router.register('api/tipo_usuario', TipoUsuarioViewSet, basename='tipo_usuario')
router.register('api/usuario', AuthUserViewSet, basename='usuario')
router.register('api/modulos', ModulosViewSet, basename='modulos')
router.register('api/permisos', PermisosViewSet, basename='permisos')

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/send-reset-password', views.send_reset_password_email, name='reset_password'),
    path('api/reset-password', views.restore_password, name='reset_password'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/update-profile-picture/<int:user_id>/', UpdateProfilePictureView.as_view(), name='update-profile-picture'),
]