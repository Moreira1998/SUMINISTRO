from django.urls import path
from apps.producto.views import ProductoList, ProductoNew, ProductoUpdate, ProductoDelete

app_name = 'producto'

urlpatterns = [

    # -------------------------------------------------------->
    # Path Producto

    path('productoList', ProductoList.as_view(), name='producto_list'),
    path('productoNew', ProductoNew.as_view(), name='producto_new'),
    path('productoUpdate/<str:pk>', ProductoUpdate.as_view(), name='producto_update'),
    path('productoDelete/<str:pk>', ProductoDelete.as_view(), name='producto_delete'),

]
