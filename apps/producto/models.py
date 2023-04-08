from django.db import models


# Create your models here.
# ------------------------------------------------------------------------------------>
# Model Proveedor

class Proveedor(models.Model):
    FORMA_PAGO_PV = (
        ('Contado', 'Contado'),
        ('Credito', 'Credito'),
    )
    nombre = models.CharField(max_length=100, null=True)
    ruc = models.CharField(max_length=100, null=True, blank=True)
    vendedor = models.CharField(max_length=100, null=True)
    telefono = models.CharField(max_length=100, null=True)
    dirreccion = models.CharField(max_length=100, null=True)
    formaPago = models.CharField(max_length=100, null=True, choices=FORMA_PAGO_PV)

    def __str__(self):
        return str(self.nombre)


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
    status = models.BooleanField()

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'producto'

    def __str__(self):
        return '%s - %s' % (self.nombre, self.marca)


# ------------------------------------------------------------------------------------->
# Model Factura


class Factura(models.Model):

    FORMA_PAGO_FAC = (
        ('Transferencia', 'Transferencia'),
        ('Cheque', 'Cheque'),
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta'),
    )

    MONEDA = (
        ('Córdobas', 'Córdobas'),
        ('Dólares', 'Dólares'),
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
    status = models.BooleanField(default=False)
    fecha = models.DateField()

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Factura'

    def TotalDolar(self):
        if self.moneda == 'Córdobas':
            dolar = self.total / self.tipoCambio
            return round(dolar, 2)
        if self.moneda == 'Dólares':
            dolar = self.total * self.tipoCambio
            return round(dolar, 2)
        pass

    def __str__(self):
        return str(self.numFac)


# ------------------------------------------------------------------------------------->
# Model Factura

class DetalleFactura(models.Model):
    numFac = models.ForeignKey(Factura, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField()
    precio = models.FloatField()

    class Meta:
        verbose_name = 'DetalleFactura'
        verbose_name_plural = 'DetalleFactura'
    def __str__(self):
        return str(self.numFac)