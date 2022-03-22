from django.db import models
# Create your models here.
from apps.producto.models import Producto


class Solicitud(models.Model):
    AREA = (
        ('CONTABILIDAD', 'CONTABILIDAD'),
        ('OPERACIONES', 'OPERACIONES'),
        ('SERVICIO AL CLIENTE', 'SERVICIO AL CLIENTE'),
        ('ADMINISTRACION', 'ADMINISTRACION')
    )
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField(null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    area = models.CharField(max_length=100, null=True, choices=AREA)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'producto'

    def __str__(self):
        return str(self.producto)
