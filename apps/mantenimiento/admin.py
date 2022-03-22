from django.contrib import admin
from apps.mantenimiento.models import Proveedor, Factura, Empresa, Mant, Mantenimiento

admin.site.register(Proveedor)
admin.site.register(Factura)
admin.site.register(Empresa)
admin.site.register(Mant)
admin.site.register(Mantenimiento)
