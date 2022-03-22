from django.db import models

# ------------------------------------------------------------------------------------->
# Model Proveedor


class Proveedor(models.Model):
    FORMA_PAGO_PV = (
        ('DE CONTADO', 'DE CONTADO'),
        ('Credito', 'Credito'),
    )
    nombre = models.CharField(max_length=100, null=True)
    ruc = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True)
    dirreccion = models.CharField(max_length=100, null=True)
    formaPago = models.CharField(max_length=100, null=True, choices=FORMA_PAGO_PV)

    def __str__(self):
        return str(self.nombre)

# ------------------------------------------------------------------------------------->
# Model Factura


class Factura(models.Model):
    FORMA_PAGO_FAC = (
        ('TRANSFERENCIA', 'TRANSFERENCIA'),
        ('CHEQUE', 'CHEQUE'),
        ('EFECTIVO', 'EFECTIVO'),
        ('TARJETA', 'TARJETA'),
    )
    MONEDA = (
        ('CORDOBAS', 'CORDOBAS'),
        ('DOLARES', 'DOLARES'),
    )
    numFac = models.CharField(max_length=30, primary_key=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    moneda = models.CharField(max_length=100, null=True, choices=MONEDA)
    iva = models.FloatField()
    subTotal = models.FloatField()
    total = models.FloatField()
    tipoCambio = models.FloatField()
    formaPago = models.CharField(max_length=100, null=True, choices=FORMA_PAGO_FAC)
    detalle = models.CharField(max_length=100, null=True)
    fecha = models.DateField()

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Factura'

    def TotalDolar(self):
        if self.moneda == 'CORDOBAS':
            dolar = self.total / self.tipoCambio
            return round(dolar, 2)
        if self.moneda == 'DOLARES':
            dolar = self.total * self.tipoCambio
            return round(dolar, 2)
        pass
    
    def __str__(self):
        return str(self.numFac)


# ------------------------------------------------------------------------------------->
# Model Empresa


class Empresa(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Empresas'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre


# ------------------------------------------------------------------------------------->
# Model Empresa


class Mant(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Mantenimientos'
        verbose_name_plural = 'Mantenimientos'

    def __str__(self):
        return self.nombre


# ------------------------------------------------------------------------------------->
# Model Mantenimiento


class Mantenimiento(models.Model):
    mant = models.ForeignKey(Mant, on_delete=models.CASCADE, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    autorizado = models.CharField(max_length=100, null=True)
    realizado = models.CharField(max_length=100, null=True)
    factura = models.ManyToManyField(Factura, null=True, blank=True)
    comentario = models.CharField(max_length=100, null=True)
    fecha = models.DateField()

    def __str__(self):
        return str(self.mant)



