from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.mantenimiento.forms import ProveedorForm, FacturaForm, MantenimientoForm
from apps.mantenimiento.models import Proveedor, Factura, Mantenimiento
from django.urls import reverse_lazy


# ------------------------------------------------------------------------------------>
# view Proveedor


class ProveedorList(ListView):
    model = Proveedor
    template_name = 'mantenimiento/proveedor/proveedor_list.html'
    context_object_name = 'proveedor_list'
    queryset = Proveedor.objects.all()


class ProveedorNew(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'mantenimiento/proveedor/proveedor_form.html'
    success_url = reverse_lazy('mantenimiento:proveedor_list')


class ProveedorDetail(DetailView):
    model = Proveedor
    template_name = 'mantenimiento/proveedor/proveedor_detail.html'
    queryset = Proveedor.objects.all()


class ProveedorUpdate(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'mantenimiento/proveedor/proveedor_form.html'
    success_url = reverse_lazy('mantenimiento:proveedor_list')


class ProveedorDelete(DeleteView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'mantenimiento/proveedor/proveedor_delete.html'
    success_url = reverse_lazy('mantenimiento:proveedor_list')


# ------------------------------------------------------------------------------------>
# view Factura


class FacturaList(ListView):
    model = Factura
    template_name = 'mantenimiento/factura/factura_list.html'
    context_object_name = 'factura_list'
    queryset = Factura.objects.all()


class FacturaNew(CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'mantenimiento/factura/factura_form.html'
    success_url = reverse_lazy('mantenimiento:factura_list')


class FacturaUpdate(UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'mantenimiento/factura/factura_form.html'
    success_url = reverse_lazy('mantenimiento:factura_list')


class FacturaDetail(DetailView):
    model = Factura
    template_name = 'mantenimiento/factura/factura_detail.html'
    queryset = Factura.objects.all()


class FacturaDelete(DeleteView):
    model = Factura
    form_class = FacturaForm
    template_name = 'mantenimiento/factura/factura_delete.html'
    success_url = reverse_lazy('mantenimiento:factura_list')


# ------------------------------------------------------------------------------------>
# view Mantenimiento


class MantenimientoList(ListView):
    model = Mantenimiento
    template_name = 'mantenimiento/mantenimiento/mantenimiento_list.html'
    context_object_name = 'mantenimiento_list'
    queryset = Mantenimiento.objects.all()


class MantenimientoNew(CreateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/mantenimiento/mantenimiento_form.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento_list')


class MantenimientoUpdate(UpdateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/mantenimiento/mantenimiento_form.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento_list')


class MantenimientoDetail(DetailView):
    model = Mantenimiento
    template_name = 'mantenimiento/mantenimiento/mantenimiento_detail.html'
    queryset = Mantenimiento.objects.all()


class MantenimientoDelete(DeleteView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/mantenimiento/mantenimiento_delete.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento_list')

