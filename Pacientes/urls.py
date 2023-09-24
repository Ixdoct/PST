from django.urls import path
from . import views
urlpatterns = [
    ##Inicio
    path('', views.home, name='home'),
    
    ##Horarios
    path('horarios/', views.horarios, name="horarios"),

    ##Horarios
    path('acd/', views.acd, name="acd"),

    ##Logout
    path('exit/', views.exit, name="exit"),

    ##Panel de Gestiones
    path('gestiones/', views.gestiones, name="gestiones"),

    ##Pacientes
    path('gestiones/gestionPacientes', views.listarPacientes),
    path('registrarPacientes/', views.registrarPacientes),
    path('gestiones/editarPacientes/<cedula>', views.editarPacientes),
    path('edicionPacientes/', views.edicionPacientes),
    path('gestiones/eliminarPacientes/<cedula>', views.eliminarPacientes),
    
    ##Productos
    path('gestiones/gestionProductos', views.listarProductos),
    path('gestiones/proveedor/', views.obtenerProveedores, name='obtenerProveedores'),
    path('registrarProductos/', views.registrarProductos),
    path('gestiones/editarProductos/<codigo>', views.editarProductos),
    path('edicionProductos/', views.edicionProductos),
    path('gestiones/eliminarProductos/<codigo>', views.eliminarProductos),

    ##Proveedores
    path('gestiones/gestionProveedores', views.listarProveedores),
    path('registrarProveedores/', views.registrarProveedores),
    path('gestiones/editarProveedores/<cedula_prov>', views.editarProveedores),
    path('edicionProveedores/', views.edicionProveedores),
    path('gestiones/eliminarProveedores/<cedula_prov>', views.eliminarProveedores),
]
    


