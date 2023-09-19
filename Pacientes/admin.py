from django.contrib import admin
from .models import Pacientes, Proveedores, Productos, Examenes
# Register your models here.

class PacientesAdmin(admin.ModelAdmin):
    ordering = ['nombre']

class ProveedoresAdmin(admin.ModelAdmin):
    search_fields = ('cedula_prov'),
    ordering = ['nombre_prov']

class ProductosAdmin(admin.ModelAdmin):
    ordering = ['nombrep']
    autocomplete_fields = ['proveedor']

admin.site.register(Pacientes, PacientesAdmin)
admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Examenes)