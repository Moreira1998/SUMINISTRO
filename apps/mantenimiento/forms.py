from django import forms
from apps.mantenimiento.models import Proveedor, Factura, Mantenimiento


# ------------------------------------------------------------------------------------>
# forms Proveedor


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'ruc': 'RUC',
            'telefono': 'Teléfono',
            'dirreccion': 'Dirección',
            'formaPago': 'Forma de pago',
        }
        widgets = {
            'formaPago': forms.Select(attrs={'class': 'form-control'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# ------------------------------------------------------------------------------------>
# view Factura


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'
        labels = {
            'numFac': 'Número de Requisa',
            'proveedor': 'Proveedor',
            'moneda': 'Tipo de moneda',
            'iva': 'Detalle IVA',
            'subTotal': 'Subtotal',
            'total': 'Total córdobas',
            'tipoCambio': 'Tipo de cambio',
            'formaPago': 'Forma de pago',
            'detalle': 'Detalle Requisa',
            'fecha': 'Fecha Requisa',

        }
        widgets = {
            'numFac': forms.TextInput(attrs={'class': 'form-control'}),
            'iva': forms.NumberInput(attrs={'class': 'form-control'}),
            'moneda': forms.Select(attrs={'class': 'form-control'}),
            'subTotal': forms.NumberInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipoCambio': forms.NumberInput(attrs={'class': 'form-control'}),
            'formaPago': forms.Select(attrs={'class': 'form-control'}),
            'detalle': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),
            'proveedor': forms.Select(attrs={'class': 'w-100 form-control js-example-basic-single'})
        }


# ------------------------------------------------------------------------------------>
# forms Proveedor


class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
        labels = {
            'mant': 'Mantenimiento',
            'empresa': 'Empresa',
            'autorizado': 'Autorizado por',
            'realizado': 'Realizado por',
            'factura': 'Requisa',
            'comentario': 'Comentario',
            'fecha': 'Fecha',
        }
        widgets = {
            'mant': forms.Select(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'autorizado': forms.TextInput(attrs={'class': 'form-control'}),
            'realizado': forms.TextInput(attrs={'class': 'form-control'}),
            'factura': forms.SelectMultiple(attrs={'class': 'w-100 form-control js-example-basic-multiple',
                                                   'multiple': 'multiple',
                                                   }),
            'comentario': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),

        }
