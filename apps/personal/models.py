from django.db import models
from django.contrib.auth.models import User


# ------------------------------------------------------------------------------------>
# Model Area


class Area(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Area'

    def __str__(self):
        return self .nombre


# ------------------------------------------------------------------------------------>
# Model Rol


class Rol(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Rol'

    def __str__(self):
        return self .nombre


# ------------------------------------------------------------------------------------->
# Model Personal


class Personal(models.Model):
    idPersonal = models.CharField(max_length=30, primary_key=True)
    nombre = models.CharField(max_length=100, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'

    def __str__(self):
        return self.idPersonal
