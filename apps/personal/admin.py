from django.contrib import admin
from apps.personal.models import Personal, Rol, Area

# Register your models here.
admin.site.register(Personal)
admin.site.register(Rol)
admin.site.register(Area)