from django.contrib import admin
from apps.producto.models import Producto, Marca, Categoria

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Marca)