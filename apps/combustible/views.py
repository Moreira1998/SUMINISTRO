from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from apps.combustible.forms import VehiculoForm, ConsumoForm
from apps.combustible.models import Vehiculo, Consumo


# ------------------------------------------------------------------------------------>
# view Vehiculo


class VehiculoList(ListView):
    model = Vehiculo
    template_name = 'combustible/vehiculo/vehiculo_list.html'
    context_object_name = 'vehiculo_list'
    queryset = Vehiculo.objects.all()


class VehiculoNew(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'combustible/vehiculo/vehiculo_form.html'
    success_url = reverse_lazy('combustible:vehiculo_list')


class VehiculoUpdate(UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'combustible/vehiculo/vehiculo_form.html'
    success_url = reverse_lazy('combustible:vehiculo_list')


class VehiculoDetail(DetailView):
    model = Vehiculo
    template_name = 'combustible/vehiculo/vehiculo_detail.html'
    queryset = Vehiculo.objects.all()


class VehiculoDelete(DeleteView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'combustible/vehiculo/vehiculo_delete.html'
    success_url = reverse_lazy('combustible:vehiculo_list')


# ------------------------------------------------------------------------------------>
# view Combustible


class ConsumoList(ListView):
    model = Consumo
    template_name = 'combustible/consumo/consumo_list.html'
    context_object_name = 'consumo_list'
    queryset = Consumo.objects.all()


class ConsumoNew(CreateView):
    model = Consumo
    form_class = ConsumoForm
    template_name = 'combustible/consumo/consumo_form.html'
    success_url = reverse_lazy('combustible:consumo_list')


class ConsumoDetail(DetailView):
    model = Consumo
    template_name = 'combustible/consumo/consumo_detail.html'
    queryset = Consumo.objects.all()


class ConsumoUpdate(UpdateView):
    model = Consumo
    form_class = ConsumoForm
    template_name = 'combustible/consumo/consumo_form.html'
    success_url = reverse_lazy('combustible:consumo_list')


class ConsumoDelete(DeleteView):
    model = Consumo
    form_class = ConsumoForm
    template_name = 'combustible/consumo/consumo_delete.html'
    success_url = reverse_lazy('combustible:consumo_list')

