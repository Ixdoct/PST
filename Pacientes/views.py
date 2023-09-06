from django.shortcuts import render, redirect
from .models import Pacientes, Productos, Proveedores
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
TEMPLATE_DIRS = {
    'os.path.join(BASE_DIR, "templates")'
}
#Inicio
def index(request):
    return render(request, "index.html")
#PACIENTES
def listarPacientes(request):
    pacientesListados = Pacientes.objects.all()
    messages.success(request, '¡Pacientes listados!')
    return render(request, "Pacientes/gestionPacientes.html", {"Pacientes" : pacientesListados})

def registrarPacientes(request):
    cedula=request.POST['txtCedula']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    edad=request.POST['txtEdad']

    pacientes = Pacientes.objects.create(cedula=cedula, nombre=nombre, apellido=apellido, edad=edad)
    messages.success(request, '¡Paciente Registrado!')
    return redirect('http://127.0.0.1:8000/gestionPacientes')

def editarPacientes(request, cedula):
    pacientes = Pacientes.objects.get(cedula=cedula)
    return render(request, "Pacientes/editarPacientes.html", {"pacientes" : pacientes})

def edicionPacientes(request):
    cedula=request.POST['txtCedula']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    edad=request.POST['txtEdad']

    pacientes = Pacientes.objects.get(cedula=cedula)
    pacientes.cedula = cedula
    pacientes.nombre = nombre
    pacientes.apellido = apellido
    pacientes.edad = edad
    pacientes.save()

    messages.success(request, '¡Paciente Actualizado!')

    return redirect('http://127.0.0.1:8000/gestionPacientes')

def eliminarPacientes(request, cedula):
    pacientes = Pacientes.objects.get(cedula=cedula)
    pacientes.delete()
    messages.success(request, '¡Paciente Eliminado!')
    return redirect("http://127.0.0.1:8000/gestionPacientes")

####PACIENTES

####PRODUCTOS

def listarProductos(request):
    productosListados = Productos.objects.all()
    messages.success(request, '¡Productos listados!')
    return render(request, "Insumos/gestionProductos.html", {"Productos" : productosListados})

def registrarProductos(request):
    codigo=request.POST['txtCodigo']
    proveedor=request.POST['txtProveedor']
    nombrep=request.POST['txtNombre']
    cantidad=request.POST['txtCantidad']

    productos = Productos.objects.create(codigo=codigo, proveedor=proveedor, nombrep=nombrep, cantidad=cantidad)
    messages.success(request, '¡Producto Registrado!')
    return redirect('http://127.0.0.1:8000/gestionProductos')

def editarProductos(request, codigo):
    productos = Productos.objects.get(codigo=codigo)
    return render(request, "Insumos/editarProductos.html", {"productos" : productos})

def edicionProductos(request):
    codigo=request.POST['txtCodigo']
    proveedor=request.POST['txtProveedor']
    nombrep=request.POST['txtNombre']
    cantidad=request.POST['txtCantidad']

    productos = Productos.objects.get(codigo=codigo)
    productos.codigo = codigo
    productos.proveedor = proveedor
    productos.nombrep = nombrep
    productos.cantidad = cantidad
    productos.save()

    messages.success(request, '¡Producto Actualizado!')

    return redirect('http://127.0.0.1:8000/gestionProductos')

def eliminarProductos(request, codigo):
    productos = Productos.objects.get(codigo=codigo)
    productos.delete()
    messages.success(request, '¡Producto Eliminado!')
    return redirect("http://127.0.0.1:8000/gestionProductos")

###PRODUCTOS

###PROVEEDORES
def listarProveedores(request):
    proveedoresListados = Proveedores.objects.all()
    messages.success(request, '¡Proveedores listados!')
    return render(request, "Proveedores/gestionProveedores.html", {"Proveedores" : proveedoresListados})

def registrarProveedores(request):
    cedula=request.POST['txtCedula']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    ciudad=request.POST['txtCiudad']

    proveedores = Proveedores.objects.create(cedula=cedula, nombre=nombre, apellido=apellido, ciudad=ciudad)
    messages.success(request, '¡Proveedor Registrado!')
    return redirect('http://127.0.0.1:8000/gestionProveedores')

def editarProveedores(request, cedula):
    proveedores = Proveedores.objects.get(cedula=cedula)
    return render(request, "Proveedores/editarProveedores.html", {"proveedores" : proveedores})

def edicionProveedores(request):
    cedula=request.POST['txtCedula']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    ciudad=request.POST['txtCiudad']

    proveedores = Proveedores.objects.get(cedula=cedula)
    proveedores.cedula = cedula
    proveedores.nombre = nombre
    proveedores.apellido = apellido
    proveedores.ciudad = ciudad
    proveedores.save()

    messages.success(request, '¡Proveedor Actualizado!')

    return redirect('http://127.0.0.1:8000/gestionProveedores')

def eliminarProveedores(request, cedula):
    proveedores = Proveedores.objects.get(cedula=cedula)
    proveedores.delete()
    messages.success(request, '¡Proveedor Eliminado!')
    return redirect("http://127.0.0.1:8000/gestionProveedores")