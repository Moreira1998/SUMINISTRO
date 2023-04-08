from django import forms
from apps.combustible.models import Vehiculo, Consumo


# -------------------------------------------------------->
# Forms Vehiculo


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        labels = {
            'placa': 'Número de placa',
            'vehiculo': 'Vehículo',
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
            'rendimiento': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# -------------------------------------------------------->
# Forms consumo


class ConsumoForm(forms.ModelForm):
    class Meta:
        model = Consumo
        fields = '__all__'
        labels = {
            'vehiculo': 'Seleccione el vehículo',
            'factura': 'Número de factura',
            'monto': 'Monto facturado',
            'litros': 'Litros',
            'km_inicio': 'Km inicial',
            'km_fin': 'Km final',
            'fecha': 'Fecha',
        }
        widgets = {
            'vehiculo': forms.Select(attrs={'class': 'w-100 form-control js-example-basic-single'}),
            'litros': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'factura': forms.TextInput(attrs={'class': 'form-control', 'min': 0}),
            'km_inicio': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'km_fin': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'fecha': forms.DateInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),
        }

