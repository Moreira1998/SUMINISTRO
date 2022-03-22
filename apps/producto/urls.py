from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.producto.views import ProductoList, ProductoNew, ProductoUpdate, ProductoDelete, MarcaList, MarcaNew, \
    MarcaUpdate, MarcaDelete, CategoriaList, CategoriaNew, CategoriaUpdate, CategoriaDelete, ProveedorList, \
    ProveedorDetail, ProveedorNew, FacturaList, FacturaNew, DespacharPoducto, ProveedorDelete, ProveedorUpdate, \
    FacturaUpdate, FacturaDetail, FacturaDelete, ProductoDetail, FacturaPendienteList

app_name = 'producto'

urlpatterns = [

    # -------------------------------------------------------->
    # Path producto

    path('productoList', login_required(ProductoList.as_view()), name='producto_list'),
    path('productoNew', login_required(ProductoNew.as_view()), name='producto_new'),
    path('productoDetail/<str:pk>', login_required(ProductoDetail.as_view()), name='producto_detail'),
    path('productoUpdate/<str:pk>', login_required(ProductoUpdate.as_view()), name='producto_update'),
    path('productoDelete/<str:pk>', login_required(ProductoDelete.as_view()), name='producto_delete'),

    # -------------------------------------------------------->
    # Path Marca

    path('marcaList', login_required(MarcaList.as_view()), name='marca_list'),
    path('marcaNew', login_required(MarcaNew.as_view()), name='marca_new'),
    path('marcaUpdate/<str:pk>', login_required(MarcaUpdate.as_view()), name='marca_update'),
    path('marcaDelete/<str:pk>', login_required(MarcaDelete.as_view()), name='marca_delete'),

    # -------------------------------------------------------->
    # Path Categoria

    path('categoriaList', login_required(CategoriaList.as_view()), name='categoria_list'),
    path('categoriaNew', login_required(CategoriaNew.as_view()), name='categoria_new'),
    path('categoriaUpdate/<str:pk>', login_required(CategoriaUpdate.as_view()), name='categoria_update'),
    path('categoriaDelete/<str:pk>', login_required(CategoriaDelete.as_view()), name='categoria_delete'),

    # -------------------------------------------------------->
    # Path Proveedor

    path('proveedorList', login_required(ProveedorList.as_view()), name='proveedor_list'),
    path('proveedorNew', login_required(ProveedorNew.as_view()), name='proveedor_new'),
    path('proveedorDetail/<str:pk>', login_required(ProveedorDetail.as_view()), name='proveedor_detail'),
    path('proveedorUpdate/<str:pk>', login_required(ProveedorUpdate.as_view()), name='proveedor_update'),
    path('proveedorDelete/<str:pk>', login_required(ProveedorDelete.as_view()), name='proveedor_delete'),

    # -------------------------------------------------------->
    # Path Factura

    path('facturaList', login_required(FacturaList.as_view()), name='factura_list'),
    path('facturaNew', login_required(FacturaNew.as_view()), name='factura_new'),
    path('facturaDetail/<str:pk>', login_required(FacturaDetail.as_view()), name='factura_detail'),
    path('facturaUpdate/<str:pk>', login_required(FacturaUpdate.as_view()), name='factura_update'),
    path('facturaDelete/<str:pk>', login_required(FacturaDelete.as_view()), name='factura_delete'),
    path('facturaPendiente', login_required(FacturaPendienteList.as_view()), name='factura_pendiente'),
    path('despachar/<int:pk>', login_required(DespacharPoducto.as_view()), name='factura_stock'),


]
