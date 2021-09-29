from django import forms
from django.contrib.auth.models import User
from apps.producto.models import Producto
from apps.solicitud.models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        labels = {
            'producto': 'Producto',
            'cantidad': 'Cantidad',
            'fecha': 'Fecha',
            'area': 'Area'
        }
        widgets = {
            'producto': forms.RadioSelect(),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(),
            'area': forms.Select(attrs={'class': 'form-control'}),
        }
