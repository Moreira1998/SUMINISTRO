from django.db import models


# Create your models here.
# ------------------------------------------------------------------------------------>
# Model Marca


class Marca(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marca'

    def __str__(self):
        return self.nombre


# ------------------------------------------------------------------------------------>
# Model Marca


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoria'

    def __str__(self):
        return self.nombre


# ------------------------------------------------------------------------------------>
# Model Product


class Producto(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=100, null=True)
    cantidad = models.IntegerField(null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Producto'

    def __str__(self):
        return self.nombre
