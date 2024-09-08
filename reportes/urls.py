from rest_framework import routers
from .views import ReporteBeneficiadosViewSet, ReporteDeudasViewSet, ReporteMetodoPagoViewSet, ReporteIngresosViewSet, TipoReportesViewSet, HistorialReportesViewSet, PermisosReportesViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register('api/tipo-reportes', TipoReportesViewSet, basename='tipo-reportes')
router.register('api/historial-reportes', HistorialReportesViewSet, basename='historial-reportes')
router.register('api/permisos-reportes', PermisosReportesViewSet, basename='permisos-reportes')
router.register('api/reporte-beneficiados', ReporteBeneficiadosViewSet, basename='reporte-beneficiados')
router.register('api/reporte-deudas', ReporteDeudasViewSet, basename='reporte-deudas')
router.register('api/reporte-metodo-pago', ReporteMetodoPagoViewSet, basename='reporte-metodo-pago')
router.register('api/reporte-ingresos', ReporteIngresosViewSet, basename='reporte-ingresos')

urlpatterns = [
    path('', include(router.urls)),
]
