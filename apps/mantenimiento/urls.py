from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter

# -------------------------------------------------------->
# Routers ApI
from apps.mantenimiento.reports import ReporteMantenimiento
from apps.mantenimiento.views import (ProveedorList, ProveedorNew,
                                      ProveedorUpdate, ProveedorDelete,
                                      FacturaList, FacturaNew, FacturaUpdate, FacturaDelete, MantenimientoList,
                                      MantenimientoNew, MantenimientoDelete, MantenimientoUpdate, MantenimientoDetail,
                                      FacturaDetail, ProveedorDetail)

routers = DefaultRouter()

app_name = 'mantenimiento'

urlpatterns = [

    # -------------------------------------------------------->
    # Path Routers API

    path('api/', include(routers.urls)),

    # -------------------------------------------------------->
    # Path Mantenimiento

    path('proveedorList', login_required(ProveedorList.as_view()), name='proveedor_list'),
    path('vehiculoNew', login_required(ProveedorNew.as_view()), name='proveedor_new'),
    path('proveedorDetail/<int:pk>', login_required(ProveedorDetail.as_view()), name='proveedor_detail'),
    path('vehiculoUpdate/<int:pk>', login_required(ProveedorUpdate.as_view()), name='proveedor_update'),
    path('vehiculoDelete/<str:pk>', login_required(ProveedorDelete.as_view()), name='proveedor_delete'),


    # -------------------------------------------------------->
    # Path Factura

    path('facturaList', login_required(FacturaList.as_view()), name='factura_list'),
    path('facturaNew', login_required(FacturaNew.as_view()), name='factura_new'),
    path('facturaDetail/<int:pk>', login_required(FacturaDetail.as_view()), name='factura_detail'),
    path('facturaUpdate/<str:pk>', login_required(FacturaUpdate.as_view()), name='factura_update'),
    path('facturaDelete/<str:pk>', login_required(FacturaDelete.as_view()), name='factura_delete'),

    # -------------------------------------------------------->
    # Path Mantenimiento

    path('mantenimientoList', login_required(MantenimientoList.as_view()), name='mantenimiento_list'),
    path('mantenimientoNew', login_required(MantenimientoNew.as_view()), name='mantenimiento_new'),
    path('mantenimientoDetail/<int:pk>', login_required(MantenimientoDetail.as_view()), name='mantenimiento_detail'),
    path('mantenimientoUpdate/<str:pk>', login_required(MantenimientoUpdate.as_view()), name='mantenimiento_update'),
    path('mantenimientoDelete/<str:pk>', login_required(MantenimientoDelete.as_view()), name='mantenimiento_delete'),

    # -------------------------------------------------------->
    # Path Reporte

    path('reporteMantenimiento', login_required(ReporteMantenimiento.as_view()), name='mantenimiento_reporte'),
]
