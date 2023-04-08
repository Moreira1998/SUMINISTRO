from apps.producto.forms import ProductoForm, MarcaForm, CategoriaForm, ProveedorForm, FacturaForm, DetalleFacturaForm
from apps.producto.models import Producto, Marca, Categoria, Proveedor, Factura, DetalleFactura
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, RedirectView, DetailView, TemplateView
from django.urls import reverse_lazy


# ------------------------------------------------------------------------------------>
# view Personal

class ProductoList(ListView):
    model = Producto
    template_name = 'producto/producto/producto_list.html'
    context_object_name = 'producto_list'
    queryset = Producto.objects.all()



class ProductoNew(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto/producto_form.html'
    success_url = reverse_lazy('producto:producto_list')


class ProductoDetail(DetailView):
    model = Producto
    template_name = 'producto/producto/producto_detail.html'
    queryset = Producto.objects.all()


class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto/producto_form.html'
    success_url = reverse_lazy('producto:producto_list')


class ProductoDelete(DeleteView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto/producto_delete.html'
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


# ------------------------------------------------------------------------------------>
# view Proveedor


class ProveedorList(ListView):
    model = Proveedor
    template_name = 'producto/proveedor/proveedor_list.html'
    context_object_name = 'proveedor_list'
    queryset = Proveedor.objects.all()


class ProveedorNew(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'producto/proveedor/proveedor_form.html'
    success_url = reverse_lazy('producto:proveedor_list')


class ProveedorUpdate(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'producto/proveedor/proveedor_form.html'
    success_url = reverse_lazy('producto:proveedor_list')


class ProveedorDetail(DetailView):
    model = Proveedor
    template_name = 'producto/proveedor/proveedor_detail.html'
    queryset = Proveedor.objects.all()


class ProveedorDelete(DeleteView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'producto/proveedor/proveedor_delete.html'
    success_url = reverse_lazy('producto:proveedor_list')

# ------------------------------------------------------------------------------------>
# view DetalleFactura

class DetalleFacturaList(ListView):
    model = Factura
    template_name = 'producto/factura/detalleFactura/detalleFactura_list.html'
    context_object_name = 'detalleFactura_list'
    queryset = DetalleFactura.objects.all()

class DetalleFacturaNew(CreateView):
    model = DetalleFactura
    form_class = DetalleFacturaForm
    template_name = 'producto/factura/detalleFactura/detalleFactura_form.html'
    success_url = reverse_lazy('producto:detalleFactura_list')


class DetalleFacturaUpdate(UpdateView):
    model = DetalleFactura
    form_class = DetalleFacturaForm
    template_name = 'producto/factura/detalleFactura/detalleFactura_form.html'
    success_url = reverse_lazy('producto:detalleFactura_list')

class DetalleFacturaDelete(DeleteView):
    model = DetalleFactura
    form_class = DetalleFacturaForm
    template_name = 'producto/factura/detalleFactura/detalleFactura_delete.html'
    success_url = reverse_lazy('producto:detalleFactura_list')


# ------------------------------------------------------------------------------------>
# view Factura


class FacturaList(ListView):
    model = Factura
    template_name = 'producto/factura/factura_list.html'
    context_object_name = 'factura_list'
    queryset = Factura.objects.all()


class FacturaNew(CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'producto/factura/factura_form.html'
    success_url = reverse_lazy('producto:detalleFactura_new')


class FacturaDetail(DetailView):
    model = Factura
    template_name = 'producto/factura/factura__detail.html'
    queryset = Factura.objects.all()


class FacturaUpdate(UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'producto/factura/factura_form.html'
    success_url = reverse_lazy('producto:factura_list')


class FacturaDelete(DeleteView):
    model = Factura
    form_class = FacturaForm
    template_name = 'producto/factura/factura_delete.html'
    success_url = reverse_lazy('producto:factura_list')

# ------------------------------------------------------------------------------------>
# view Factura Pendiente

class FacturaPendienteList(ListView):
    model = Factura
    template_name = "producto/factura/facturaPendiente.html"
    context_object_name = 'factura_list'
    queryset = Factura.objects.all()


# ------------------------------------------------------------------------------------>
# view Despacho

class DespacharPoducto(RedirectView):
    """ Despacha una factura sumando la cantidad al
    stock del producto.
    la vista redirige a la lista de productos """
    url = reverse_lazy('producto:factura_list')

    def get(self, request, *args, **kwargs):
        # obtenemos la factura desde el id
        factura = Factura.objects.\
            prefetch_related('detallefactura_set').\
            get(numFac=self.kwargs['pk'])
        # obtenemos el id del producto desde la factura
        detalles = factura.detallefactura_set.all()
        cantidades_por_producto = {}
        for detalle in detalles:
            producto_id = detalle.producto.pk
            cantidad = detalle.cantidad
            if not cantidades_por_producto.get(producto_id):
                cantidades_por_producto[producto_id] = 0
            cantidades_por_producto[producto_id] += cantidad

        for producto_id, cantidad in cantidades_por_producto.items():
            producto = Producto.objects.filter(id=producto_id).first()
            producto.cantidad += cantidad
            producto.save()

        # Cambiamos el status
        factura.status = True
        # guardamos los cambio de solicitud
        factura.save()

        return super().get(request, *args, **kwargs)




            


