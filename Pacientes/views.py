from django.shortcuts import render, redirect
from .models import Pacientes, Productos, Proveedores
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.
TEMPLATE_DIRS = {
    'os.path.join(BASE_DIR, "templates")'
}
#Inicio
def index(request):
    return render(request, "index.html")

#PACIENTES
def listarPacientes(request):
    busqueda = request.GET.get("buscar")
    pacientesListados = Pacientes.objects.all()

    if busqueda:
        pacientesListados = Pacientes.objects.filter(
        Q(cedula = busqueda)  |
        Q(nombre__icontains = busqueda)  |
        Q(apellido__icontains = busqueda)
        ).distinct()
        
    messages.success(request, '¡Pacientes listados!')
    return render(request, "Pacientes/gestionPacientes.html", {"Pacientes" : pacientesListados})

def registrarPacientes(request):
    cedula=request.POST['txtCedula']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    edad=request.POST['txtEdad']
    sexo=request.POST['txtSexo']
    fechaNac=request.POST['txtFechaNac']
    direccion=request.POST['txtDireccion']
    lugarNac=request.POST['txtLugarNac']


    pacientes = Pacientes.objects.create(cedula=cedula, nombre=nombre, apellido=apellido, edad=edad, sexo=sexo, fechaNac=fechaNac, direccion=direccion, lugarNac=lugarNac)
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
    sexo=request.POST['txtSexo']
    fechaNac=request.POST['txtFechaNac']
    direccion=request.POST['txtDireccion']
    lugarNac=request.POST['txtLugarNac']


    pacientes = Pacientes.objects.get(cedula=cedula)
    pacientes.cedula = cedula
    pacientes.nombre = nombre
    pacientes.apellido = apellido
    pacientes.edad = edad
    pacientes.sexo = sexo
    pacientes.fechaNac = fechaNac
    pacientes.direccion = direccion
    pacientes.lugarNac = lugarNac
    pacientes.save()

    messages.success(request, '¡Paciente Actualizado!')

    return redirect('http://127.0.0.1:8000/gestionPacientes')

def eliminarPacientes(request, cedula):
    pacientes = Pacientes.objects.get(cedula=cedula)
    pacientes.delete()
    messages.success(request, '¡Paciente Eliminado!')
    return redirect("http://127.0.0.1:8000/gestionPacientes")

###################################################################################################

##PRODUCTOS

def listarProductos(request):
    busqueda = request.GET.get("buscar")
    productosListados = Productos.objects.all()

    if busqueda:
        productosListados = Productos.objects.filter(
        Q(codigo = busqueda)  |
        Q(nombrep__icontains = busqueda)  
        ).distinct()

    messages.success(request, '¡Productos listados!')
    return render(request, "Insumos/gestionProductos.html", {"Productos" : productosListados})

def obtenerProveedores(_request):
    proveedor = list(Proveedores.objects.values())

    if(len(proveedor)>0):
        data = {'message': "Success", 'proveedor':proveedor}
    else:
        data = {'message': "Not Found"}
    return JsonResponse(data)

def registrarProductos(request):
    codigo=request.POST['txtCodigo']
    proveedor = Proveedores.objects.get( cedula_prov = request.POST['txtProveedor'],)
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

##################################################################################################

##PROVEEDORES
def listarProveedores(request):
    busqueda = request.GET.get("buscar")
    proveedoresListados = Proveedores.objects.all()

    if busqueda:
        proveedoresListados = Proveedores.objects.filter(
        Q(cedula_prov = busqueda)  |
        Q(nombre_prov__icontains = busqueda)  |
        Q(apellido_prov__icontains = busqueda)
        ).distinct()

    messages.success(request, '¡Proveedores listados!')
    return render(request, "Proveedores/gestionProveedores.html", {"Proveedores" : proveedoresListados})

def registrarProveedores(request):
    cedula_prov=request.POST['txtCedulaProv']
    rif=request.POST['txtRifProv']
    nombre_prov=request.POST['txtNombreProv']
    apellido_prov=request.POST['txtApellidoProv']
    direccion_prov=request.POST['txtDireccionProv']
    telefono_prov=request.POST['txtTelefonoProv']

    proveedores = Proveedores.objects.create(cedula_prov=cedula_prov, nombre_prov=nombre_prov, apellido_prov=apellido_prov, direccion_prov=direccion_prov, rif=rif, telefono_prov=telefono_prov)
    messages.success(request, '¡Proveedor Registrado!')
    return redirect('http://127.0.0.1:8000/gestionProveedores')

def editarProveedores(request, cedula_prov):
    proveedores = Proveedores.objects.get(cedula_prov=cedula_prov)
    return render(request, "Proveedores/editarProveedores.html", {"proveedores" : proveedores})

def edicionProveedores(request):
    cedula_prov=request.POST['txtCedulaProv']
    rif=request.POST['txtRifProv']
    nombre_prov=request.POST['txtNombreProv']
    apellido_prov=request.POST['txtApellidoProv']
    direccion_prov=request.POST['txtDireccionProv']
    telefono_prov=request.POST['txtTelefonoProv']

    proveedores = Proveedores.objects.get(cedula_prov=cedula_prov)
    proveedores.cedula_prov = cedula_prov
    proveedores.rif = rif
    proveedores.nombre_prov = nombre_prov
    proveedores.apellido_prov = apellido_prov
    proveedores.direccion_prov = direccion_prov
    proveedores.telefono_prov = telefono_prov
    proveedores.save()

    messages.success(request, '¡Proveedor Actualizado!')

    return redirect('http://127.0.0.1:8000/gestionProveedores')

def eliminarProveedores(request, cedula_prov):
    proveedores = Proveedores.objects.get(cedula_prov=cedula_prov)
    proveedores.delete()
    messages.success(request, '¡Proveedor Eliminado!')
    return redirect("http://127.0.0.1:8000/gestionProveedores")

#################################################################################################