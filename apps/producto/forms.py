from django import forms
from apps.producto.models import Marca, Categoria, Producto, Proveedor, Factura, DetalleFactura


# -------------------------------------------------------->
# Forms User

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
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
            'descripcion': 'Descripción',
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
            'id': 'Id suministro',
            'nombre': 'Nombre',
            'categoria': 'Categoría',
            'marca': 'Marca',
            'cantidad': 'Cantidad',
        }
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
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
            'telefono': 'Teléfono',
            'vendedor': 'Vendedor',
            'dirreccion': 'Dirección',
            'formaPago': 'Forma de pago',
        }
        widgets = {
            'formaPago': forms.Select(attrs={'class': 'form-control'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'vendedor': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'dirreccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# ------------------------------------------------------------------------------------>
# view Factura


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'
        labels = {
            'numFac': 'Número de factura',
            'proveedor': 'Proveedor',
            'moneda': 'Tipo de moneda',
            'iva': 'Detalle IVA',
            'subTotal': 'Subtotal',
            'total': 'Total',
            'tipoCambio': 'Tipo de cambio',
            'formaPago': 'Forma de pago',
            'detalle': 'Detalle factura',
            'fecha': 'Fecha facturación',

        }
        widgets = {
            'numFac': forms.TextInput(attrs={'class': 'form-control'}),
            'iva': forms.NumberInput(attrs={'class': 'form-control'}),
            'moneda': forms.Select(attrs={'class': 'form-control'}),
            'subTotal': forms.NumberInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipoCambio': forms.NumberInput(attrs={'class': 'form-control'}),
            'formaPago': forms.Select(attrs={'class': 'form-control'}),
            'detalle': forms.Textarea(attrs={'class': 'form-control mb-4' , 'style':'height:80px'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),
            'proveedor': forms.Select(attrs={'class': 'w-100 form-control js-example-basic-single'}),
        }

# -------------------------------------------------------->
# Forms producto

class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = '__all__'
        labels = {
            'codigoProducto': 'Código suministro',
            'numFac': 'Número de factura',
            'producto': 'Suministro',
            'cantidad': 'Cantidad',
            'precio': 'Precio',
        }
        widgets = {
            'numFac': forms.Select(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }