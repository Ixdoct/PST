from django.contrib import admin
from .models import Pacientes, Proveedores, Productos, Examenes

# Register your models here.

@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    # list_display = ('cedula', 'nombre', 'apellido')
    ordering = ['nombre']

@admin.register(Proveedores)
class ProveedoresAdmin (admin.ModelAdmin):
    #list_display = ('cedula_prov', 'nombre_prov', 'apellido_prov')
    ordering = ['nombre_prov']

@admin.register(Productos)
class ProductosAdmin (admin.ModelAdmin):
    #list_display = ('codigo', 'nombrep', 'cantidad')
    ordering = ['nombrep']