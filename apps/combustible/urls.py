from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter

from apps.combustible.report import ReporteExcelConsumo
from apps.combustible.views import VehiculoList, VehiculoNew, VehiculoUpdate, VehiculoDetail, VehiculoDelete, \
    ConsumoList, ConsumoNew, ConsumoDetail, ConsumoUpdate, ConsumoDelete

# -------------------------------------------------------->
# Routers ApI

routers = DefaultRouter()

app_name = 'combustible'

urlpatterns = [

    # -------------------------------------------------------->
    # Path Routers API

    path('api/', include(routers.urls)),

    # -------------------------------------------------------->
    # Path vehiculo

    path('vehiculoList', login_required(VehiculoList.as_view()), name='vehiculo_list'),
    path('vehiculoNew', login_required(VehiculoNew.as_view()), name='vehiculo_new'),
    path('vehiculoUpdate/<str:pk>', login_required(VehiculoUpdate.as_view()), name='vehiculo_update'),
    path('vehiculoDetail/<str:pk>', login_required(VehiculoDetail.as_view()), name='vehiculo_detail'),
    path('vehiculoDelete/<str:pk>', login_required(VehiculoDelete.as_view()), name='vehiculo_delete'),

    # -------------------------------------------------------->
    # Path Consumo

    path('consumoList', login_required(ConsumoList.as_view()), name='consumo_list'),
    path('consumoNew', login_required(ConsumoNew.as_view()), name='consumo_new'),
    path('consumoDetail/<str:pk>', login_required(ConsumoDetail.as_view()), name='consumo_detail'),
    path('consumoUpdate/<str:pk>', login_required(ConsumoUpdate.as_view()), name='consumo_update'),
    path('consumoDelete/<str:pk>', login_required(ConsumoDelete.as_view()), name='consumo_delete'),
    path('reporteExcelConsumo', login_required(ReporteExcelConsumo.as_view()), name='consumo_report'),

]
