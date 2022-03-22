from django import forms
from apps.producto.models import Marca, Categoria, Producto, Proveedor, Factura


# -------------------------------------------------------->
# Forms User

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }


# -------------------------------------------------------->
# Forms User

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }


# -------------------------------------------------------->
# Forms producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        labels = {
            'id': 'Id producto',
            'nombre': 'Nombre',
            'categoria': 'Categoria',
            'marca': 'Marca',
            'cantidad': 'Cantidad',
        }
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
        }


# ------------------------------------------------------------------------------------>
# forms Proveedor


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'ruc': 'RUC',
            'telefono': 'Telefono',
            'vendedor': 'Vendedor',
            'dirreccion': 'Dirreccion',
            'formaPago': 'Forma de pago',
        }
        widgets = {
            'formaPago': forms.Select(attrs={'class': 'form-control'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'vendedor': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'dirreccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }


# ------------------------------------------------------------------------------------>
# view Factura


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'
        labels = {
            'numFac': 'Numero de factura',
            'proveedor': 'Proveedor',
            'moneda': 'Tipo de moneda',
            'iva': 'Detalle IVA',
            'subTotal': 'Subtotal',
            'total': 'Total',
            'tipoCambio': 'Tipo De Cambio',
            'formaPago': 'Forma De Pago',
            'detalle': 'Detalle factura',
            'producto': 'Producto',
            'cantidad': 'Cantidad',
            'fecha': 'Fecha Facturacion',

        }
        widgets = {
            'numFac': forms.TextInput(attrs={'class': 'form-control'}),
            'iva': forms.TextInput(attrs={'class': 'form-control'}),
            'moneda': forms.Select(attrs={'class': 'form-control'}),
            'subTotal': forms.TextInput(attrs={'class': 'form-control'}),
            'total': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoCambio': forms.TextInput(attrs={'class': 'form-control'}),
            'formaPago': forms.Select(attrs={'class': 'form-control'}),
            'detalle': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),
            'proveedor': forms.Select(attrs={'class': 'w-100 form-control js-example-basic-single'}),
            'producto': forms.Select(attrs={'class': 'w-100 form-control js-example-basic-single'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
        }
