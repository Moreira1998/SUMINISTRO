from apps.producto.forms import ProductoForm, MarcaForm, CategoriaForm
from apps.producto.models import Producto, Marca, Categoria
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# ------------------------------------------------------------------------------------>
# view Personal

class ProductoList(ListView):
    model = Producto
    template_name = 'producto/producto_list.html'
    context_object_name = 'producto_list'
    queryset = Producto.objects.all()


class ProductoNew(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('producto:producto_list')


class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('producto:producto_list')


class ProductoDelete(DeleteView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_delete.html'
    success_url = reverse_lazy('producto:producto_list')


# ------------------------------------------------------------------------------------>
# view Marca

class MarcaList(ListView):
    model = Marca
    template_name = 'producto/marca/marca_list.html'
    context_object_name = 'marca_list'
    queryset = Marca.objects.all()


class MarcaNew(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'producto/marca/marca_form.html'
    success_url = reverse_lazy('producto:marca_list')


class MarcaUpdate(UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'producto/marca/marca_form.html'
    success_url = reverse_lazy('producto:marca_list')


class MarcaDelete(DeleteView):
    model = Marca
    form_class = MarcaForm
    template_name = 'producto/marca/marca_delete.html'
    success_url = reverse_lazy('producto:marca_list')

# ------------------------------------------------------------------------------------>
# view Categoria


class CategoriaList(ListView):
    model = Categoria
    template_name = 'producto/categoria/categoria_list.html'
    context_object_name = 'categoria_list'
    queryset = Categoria.objects.all()


class CategoriaNew(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'producto/categoria/categoria_form.html'
    success_url = reverse_lazy('producto:categoria_list')


class CategoriaUpdate(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'producto/categoria/categoria_form.html'
    success_url = reverse_lazy('producto:categoria_list')


class CategoriaDelete(DeleteView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'producto/categoria/categoria_delete.html'
    success_url = reverse_lazy('producto:categoria_list')