from datetime import timezone

from django.db import models


# Create your models here.

# ------------------------------------------------------------------------------------->
# Model Vehiculo


class Vehiculo(models.Model):
    VEHICULO = (
        ('Motocicleta', 'Motocicleta'),
        ('Microbús', 'Microbús'),
        ('Camioneta', 'Camioneta'),
        ('Carro', 'Carro')
    )

    COMBUSTIBLE = (
        ('Gasolina', 'Gasolina'),
        ('Diesel', 'Diesel')
    )

    placa = models.CharField(max_length=30, primary_key=True)
    vehiculo = models.CharField(max_length=100, null=True, choices=VEHICULO)
    combustible = models.CharField(max_length=100, null=True, choices=COMBUSTIBLE)
    asignar = models.CharField(max_length=100, null=True)
    modelo = models.CharField(max_length=100, null=True)
    rendimiento = models.FloatField()

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculo'

    def __str__(self):
        return '%s, %s' % (self.placa, self.asignar)


# ------------------------------------------------------------------------------------->
# Model Consumo

class Consumo(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=True)
    factura = models.CharField(max_length=100, primary_key=True)
    fecha = models.DateField()
    monto = models.FloatField()
    litros = models.FloatField()
    km_inicio = models.FloatField()
    km_fin = models.FloatField()

    class Meta:
        verbose_name = 'Registro Vehicular'
        verbose_name_plural = 'Registro Vehicular'

    def RestaKM(self):
        km = self.km_fin - self.km_inicio
        return km

    def Rendimiento(self):
        recorrido = self.km_fin - self.km_inicio
        rendimiento = recorrido / self.litros
        return rendimiento.__round__(2)

    def __str__(self):
        return str(self.factura)
