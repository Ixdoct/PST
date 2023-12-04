from django.shortcuts import render, redirect
from .models import Pacientes, Productos, Proveedores
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db import IntegrityError

from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import TABLOID, LETTER
from datetime import datetime
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from django.http import HttpResponse
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# Create your views here.
TEMPLATE_DIRS = {
    'os.path.join(BASE_DIR, "templates")'
}
#Inicio
def home(request):
    return render(request, "home.html")

#Horarios
def horarios(request):
    return render(request, "horarios.html")

#Acerca de Nosotros
def acd(request):
    return render(request, "acd.html")

##Logout
def exit(request):
    logout(request)
    return redirect('home')

#Panel de Gestiones
@login_required
def gestiones(request):
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
    if request.method == 'POST':
        try:
            cedula=request.POST['txtCedula']
            nombre=request.POST['txtNombre']
            apellido=request.POST['txtApellido']
            edad=request.POST['txtEdad']
            sexo=request.POST['txtSexo']
            fechaNac=request.POST['txtFechaNac']
            direccion=request.POST['txtDireccion']
            lugarNac=request.POST['txtLugarNac']
            pacientes = Pacientes.objects.create(cedula=cedula, nombre=nombre, apellido=apellido, edad=edad, sexo=sexo, fechaNac=fechaNac, direccion=direccion, lugarNac=lugarNac)
        except IntegrityError:
            mensaje = 'La clave primaria ya existe'
            messages.success(request, 'Error: Cédula repetida!')
            return redirect('http://127.0.0.1:8000/gestiones/gestionPacientes', {'mensaje': mensaje})
        else:
            messages.success(request, '¡Paciente Registrado!')
            return redirect('http://127.0.0.1:8000/gestiones/gestionPacientes')
        

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

    return redirect('http://127.0.0.1:8000/gestiones/gestionPacientes')

def eliminarPacientes(request, cedula):
    pacientes = Pacientes.objects.get(cedula=cedula)
    pacientes.delete()
    messages.success(request, '¡Paciente Eliminado!')
    return redirect("http://127.0.0.1:8000/gestiones/gestionPacientes")

#Reporte
def reportePaciente(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=CEDIS-reports-pacientes.pdf'
    buffer = BytesIO()
    c = canvas.Canvas(buffer,pagesize=TABLOID)

    #Header
    c.setLineWidth(.3)
    c.setFont('Helvetica',22)
    c.drawString(30,750, 'CEDIS')

    c.setFont('Helvetica', 12)
    c.drawString(30,735, 'Report')

    c.setFont('Helvetica-Bold', 12)
    now = datetime.now()
    formatted_date = now.strftime("%d/%m/%Y")
    c.drawString(650,750, formatted_date)
    c.line(760,747,600,747)

    c.setFont('Helvetica', 20)
    c.drawString(70, 700, 'Listado de Pacientes')

    Story = []
    styles=getSampleStyleSheet()
    styleBH= styles["Normal"]
    styleBH.align= 'CENTER'
    styleBH.fontSize= 10
    Story.append(Paragraph('C.I', styles["Normal"]))
    Story.append(Paragraph('NOMBRE', styles["Normal"]))
    Story.append(Paragraph('APELLIDO', styles["Normal"]))
    Story.append(Paragraph('SEXO', styles["Normal"]))
    Story.append(Paragraph('EDAD', styles["Normal"])) 
    Story.append(Paragraph('FECHA DE NACIMIENTO', styles["Normal"])) 
    Story.append(Paragraph('DIRECCIÓN', styles["Normal"])) 
    Story.append(Paragraph('LUGAR DE NACIMIENTO', styles["Normal"])) 


    #Datos
    data = Pacientes.objects.all().values_list('cedula', 'nombre', 'apellido', 'sexo', 'edad', 'fechaNac', 'direccion', 'lugarNac')
    data_list = [list(row) for row in data]

    table = Table([Story] + data_list, colWidths=[1 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch, 1.18110236 * inch, 1.96850394 * inch, 1.96850394 * inch])
    Story.append(table)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)

    ]))

    #Add tabla al canvas
    table.wrapOn(c, 800, 600)
    table.drawOn(c, 10, 580)
    Story.append(table)
    
    c.showPage()
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

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
    if request.method == 'POST':
        try:
            codigo=request.POST['txtCodigo']
            proveedor = Proveedores.objects.get( cedula_prov = request.POST['txtProveedor'],)
            nombrep=request.POST['txtNombre']
            cantidad=request.POST['txtCantidad']
            productos = Productos.objects.create(codigo=codigo, proveedor=proveedor, nombrep=nombrep, cantidad=cantidad)
        except IntegrityError:
            mensaje = 'La clave primaria ya existe'
            messages.success(request, 'Error: Código repetido!')
            return redirect('http://127.0.0.1:8000/gestiones/gestionProductos', {'mensaje': mensaje})
        else:
            messages.success(request, '¡Producto Registrado!')
            return redirect('http://127.0.0.1:8000/gestiones/gestionProductos')

def editarProductos(request, codigo):
    productos = Productos.objects.get(codigo=codigo)
    return render(request, "Insumos/editarProductos.html", {"productos" : productos})

def edicionProductos(request):
    codigo=request.POST['txtCodigo']
    nombrep=request.POST['txtNombre']
    cantidad=request.POST['txtCantidad']

    productos = Productos.objects.get(codigo=codigo)
    productos.codigo = codigo
    productos.nombrep = nombrep
    productos.cantidad = cantidad
    productos.save()

    messages.success(request, '¡Producto Actualizado!')

    return redirect('http://127.0.0.1:8000/gestiones/gestionProductos')

def eliminarProductos(request, codigo):
    productos = Productos.objects.get(codigo=codigo)
    productos.delete()
    messages.success(request, '¡Producto Eliminado!')
    return redirect("http://127.0.0.1:8000/gestiones/gestionProductos")

#Reporte
def reporteProductos(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=CEDIS-reports-productos.pdf'
    buffer = BytesIO()
    c = canvas.Canvas(buffer,pagesize=LETTER)

    #Header
    c.setLineWidth(.3)
    c.setFont('Helvetica',22)
    c.drawString(30,750, 'CEDIS')

    c.setFont('Helvetica', 12)
    c.drawString(30,735, 'Report')

    c.setFont('Helvetica-Bold', 12)
    now = datetime.now()
    formatted_date = now.strftime("%d/%m/%Y")
    c.drawString(450,750, formatted_date)
    c.line(600,747,360,747)

    c.setFont('Helvetica', 20)
    c.drawString(70, 680, 'Listado de Productos')

    Story = []
    styles=getSampleStyleSheet()
    styleBH= styles["Normal"]
    styleBH.align= 'CENTER'
    styleBH.fontSize= 10
    Story.append(Paragraph('CÓDIGO', styles["Normal"]))
    Story.append(Paragraph('PROVEEDOR', styles["Normal"]))
    Story.append(Paragraph('NOMBRE', styles["Normal"]))
    Story.append(Paragraph('CANTIDAD', styles["Normal"]))

    #Datos
    data = Productos.objects.all().values_list('codigo', 'proveedor', 'nombrep', 'cantidad')
    data_list = [list(row) for row in data]

    table = Table([Story] + data_list, colWidths=[1.5 * inch, 1.5 * inch, 1.5 * inch, 1.5 * inch])
    Story.append(table)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)

    ]))

    #Add tabla al canvas
    table.wrapOn(c, 800, 600)
    table.drawOn(c, 40, 600)
    Story.append(table)
    
    c.showPage()
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

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
    if request.method == 'POST':
        try:
            cedula_prov=request.POST['txtCedulaProv']
            rif=request.POST['txtRifProv']
            nombre_prov=request.POST['txtNombreProv']
            apellido_prov=request.POST['txtApellidoProv']
            direccion_prov=request.POST['txtDireccionProv']
            telefono_prov=request.POST['txtTelefonoProv']
            proveedores = Proveedores.objects.create(cedula_prov=cedula_prov, nombre_prov=nombre_prov, apellido_prov=apellido_prov, direccion_prov=direccion_prov, rif=rif, telefono_prov=telefono_prov)
        except IntegrityError:
            mensaje = 'La clave primaria ya existe'
            messages.success(request, 'Error: Cédula repetida!')
            return redirect('http://127.0.0.1:8000/gestiones/gestionProveedores', {'mensaje': mensaje})
        else:
            messages.success(request, '¡Proveedor Registrado!')
            return redirect('http://127.0.0.1:8000/gestiones/gestionProveedores')

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

    return redirect('http://127.0.0.1:8000/gestiones/gestionProveedores')

def eliminarProveedores(request, cedula_prov):
    proveedores = Proveedores.objects.get(cedula_prov=cedula_prov)
    proveedores.delete()
    messages.success(request, '¡Proveedor Eliminado!')
    return redirect("http://127.0.0.1:8000/gestiones/gestionProveedores")

#Reporte
def reporteProveedores(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=CEDIS-reports-proveedores.pdf'
    buffer = BytesIO()
    c = canvas.Canvas(buffer,pagesize=TABLOID)

    #Header
    c.setLineWidth(.3)
    c.setFont('Helvetica',22)
    c.drawString(30,750, 'CEDIS')

    c.setFont('Helvetica', 12)
    c.drawString(30,735, 'Report')

    c.setFont('Helvetica-Bold', 12)
    now = datetime.now()
    formatted_date = now.strftime("%d/%m/%Y")
    c.drawString(650,750, formatted_date)
    c.line(760,747,600,747)

    c.setFont('Helvetica', 20)
    c.drawString(70, 690, 'Listado de Proveedores')

    Story = []
    styles=getSampleStyleSheet()
    styleBH= styles["Normal"]
    styleBH.align= 'CENTER'
    styleBH.fontSize= 10
    Story.append(Paragraph('C.I', styles["Normal"]))
    Story.append(Paragraph('RIF', styles["Normal"]))
    Story.append(Paragraph('NOMBRE', styles["Normal"]))
    Story.append(Paragraph('APELLIDO', styles["Normal"]))
    Story.append(Paragraph('DIRRECIÓN', styles["Normal"])) 
    Story.append(Paragraph('TELÉFONO', styles["Normal"])) 


    #Datos
    data = Proveedores.objects.all().values_list('cedula_prov', 'rif', 'nombre_prov', 'apellido_prov', 'direccion_prov','telefono_prov')
    data_list = [list(row) for row in data]

    table = Table([Story] + data_list, colWidths=[1 * inch, 1 * inch, 1 * inch, 1 * inch, 2 * inch, 2 * inch])
    Story.append(table)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)

    ]))

    #Add tabla al canvas
    table.wrapOn(c, 800, 600)
    table.drawOn(c, 70, 600)
    Story.append(table)
    
    c.showPage()
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

#################################################################################################

##Examenes 


#################################################################################################