from django.urls import path
from . import views
urlpatterns = [
    ##Inicio
    path('', views.index),
    ##Pacientes
    path('gestionPacientes', views.listarPacientes),
    path('registrarPacientes/', views.registrarPacientes),
    path('editarPacientes/<cedula>', views.editarPacientes),
    path('edicionPacientes/', views.edicionPacientes),
    path('eliminarPacientes/<cedula>', views.eliminarPacientes),
    
    ##Productos
    path('gestionProductos', views.listarProductos),
    path('proveedor/', views.obtenerProveedores, name='obtenerProveedores'),
    path('registrarProductos/', views.registrarProductos),
    path('editarProductos/<codigo>', views.editarProductos),
    path('edicionProductos/', views.edicionProductos),
    path('eliminarProductos/<codigo>', views.eliminarProductos),

    ##Proveedores
    path('gestionProveedores', views.listarProveedores),
    path('registrarProveedores/', views.registrarProveedores),
    path('editarProveedores/<cedula_prov>', views.editarProveedores),
    path('edicionProveedores/', views.edicionProveedores),
    path('eliminarProveedores/<cedula_prov>', views.eliminarProveedores),
]
    


