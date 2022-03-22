from django import forms
from apps.combustible.models import Vehiculo, Consumo


# -------------------------------------------------------->
# Forms Vehiculo


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        labels = {
            'placa': '# Placa',
            'vehiculo': 'Vehiculo',
            'combustible': 'Combustible',
            'asignar': 'Asignado a',
            'modelo': 'Modelo',
            'rendimiento': 'Rendimiento',
        }
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'combustible': forms.Select(attrs={'class': 'form-control'}),
            'asignar': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'rendimiento': forms.TextInput(attrs={'class': 'form-control'}),
        }


# -------------------------------------------------------->
# Forms consumo


class ConsumoForm(forms.ModelForm):
    class Meta:
        model = Consumo
        fields = '__all__'
        labels = {
            'vehiculo': 'Seleccione el vehiculo',
            'factura': 'Numero de factura',
            'monto': 'Monto facturado',
            'litros': 'Litros',
            'km_inicio': 'Km inicio',
            'km_fin': 'Km final',
            'fecha': 'Fecha',
        }
        widgets = {
            'vehiculo': forms.Select(attrs={'class': 'w-100 form-control js-example-basic-single'}),
            'litros': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.TextInput(attrs={'class': 'form-control'}),
            'factura': forms.TextInput(attrs={'class': 'form-control'}),
            'km_inicio': forms.TextInput(attrs={'class': 'form-control'}),
            'km_fin': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),
        }

