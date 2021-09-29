from django import forms
from apps.personal.models import Personal, Rol, Area


# -------------------------------------------------------->
# Forms User

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'
        labels = {
            'idPersonal': 'Id personal',
            'nombre': 'Nombre',
            'usuario': 'Usuario',
            'rol': 'Rol',
            'area': 'Area',
        }
        widgets = {
            'idPersonal': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'area': forms.Select(attrs={'class': 'form-control'}),
        }


# -------------------------------------------------------->
# Forms Rol

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = (
            'nombre',
            'descripcion',
        )
        labels = {
            'nombre': 'Nombre Del Rol',
            'descripcion': 'Descripcion del rol',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }


# -------------------------------------------------------->
# Forms Area

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = (
            'nombre',
            'descripcion',
        )
        labels = {
            'nombre': 'Nombre Del Rol',
            'descripcion': 'Descripcion del rol',
        }