from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.producto.views import ProductoList, ProductoNew, ProductoUpdate, ProductoDelete, MarcaList, MarcaNew, \
    MarcaUpdate, MarcaDelete, CategoriaList, CategoriaNew, CategoriaUpdate, CategoriaDelete

app_name = 'producto'

urlpatterns = [

    # -------------------------------------------------------->
    # Path producto

    path('productoList', login_required(ProductoList.as_view()), name='producto_list'),
    path('productoNew', login_required(ProductoNew.as_view()), name='producto_new'),
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

]
