from django import forms
from django.contrib.auth.models import User

from apps.personal.models import Personal, Rol, Area


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'username': 'Nombre de usuario',
            'last_name': 'Nombre',
            'first_name': 'Apellido',
            'password': 'Password',
            'email': 'Correo electrónico'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


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
            'area': 'Área',
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
            'nombre': 'Nombre del Rol',
            'descripcion': 'Descripción del rol',
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
            'nombre': 'Nombre del Rol',
            'descripcion': 'Descripción del rol',
        }