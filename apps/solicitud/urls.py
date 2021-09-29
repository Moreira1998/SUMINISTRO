from django.urls import path

from apps.solicitud.views import SolicitudList, SolicitudNew, EstadoSolicitudList, SolicitudUpdate, SolicitudDelete, \
    DespacharSolicitud, ReporteExcelSolicitud, ReporteList

app_name = 'solicitud'

urlpatterns = [
    # -------------------------------------------------------->
    # Path Personal

    path('solicitudList', SolicitudList.as_view(), name='solicitud_list'),
    path('estadoList', EstadoSolicitudList.as_view(), name='estadoSolicitud_list'),
    path('solicitudNew', SolicitudNew.as_view(), name='solicitud_new'),
    path('solicitudUpdate/<str:pk>', SolicitudUpdate.as_view(), name='solicitud_update'),
    path('solicitudDelete/<str:pk>', SolicitudDelete.as_view(), name='solicitud_delete'),
    path('despachark/<int:pk>', DespacharSolicitud.as_view(), name='solicitud_stock'),
    path('reporte_excel_solicitudes', ReporteExcelSolicitud.as_view(), name='solicitud_reporte'),
    path('reporte_excel', ReporteList.as_view(), name='solicitud_reporte_List'),

]
