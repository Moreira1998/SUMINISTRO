from django.db import models
from apps.personal.models import Area
# Create your models here.
from apps.producto.models import Producto


class Solicitud(models.Model):

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField(null=True, blank=True )
    fecha = models.DateField(auto_now_add=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True )
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'producto'

    def __str__(self):
        return str(self.producto)
