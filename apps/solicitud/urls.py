from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.solicitud.views import SolicitudList, SolicitudNew, EstadoSolicitudList, SolicitudUpdate, SolicitudDelete, \
    DespacharSolicitud, ReporteExcelSolicitud, ReporteFiltrar, ReporteExcelAprobados, ReporteExcelProductos

app_name = 'solicitud'

urlpatterns = [
    # -------------------------------------------------------->
    # Path Personal

    path('solicitudList', login_required(SolicitudList.as_view()), name='solicitud_list'),
    path('estadoList', login_required(EstadoSolicitudList.as_view()), name='estadoSolicitud_list'),
    path('solicitudNew', login_required(SolicitudNew.as_view()), name='solicitud_new'),
    path('solicitudUpdate/<str:pk>', login_required(SolicitudUpdate.as_view()), name='solicitud_update'),
    path('solicitudDelete/<str:pk>', login_required(SolicitudDelete.as_view()), name='solicitud_delete'),
    path('despachark/<int:pk>', login_required(DespacharSolicitud.as_view()), name='solicitud_stock'),
    path('reporteExcel', login_required(ReporteExcelSolicitud.as_view()), name='solicitud_reporte'),
    path('reporteExcelAprobados', login_required(ReporteExcelAprobados.as_view()), name='aprobados_reporte'),
    path('reporteExcelProductos', login_required(ReporteExcelProductos.as_view()), name='productos_reporte'),
    path('reporteFiltrar', login_required(ReporteFiltrar.as_view()), name='filtrar_reporte'),

]
