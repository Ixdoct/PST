from django.db import models
# Modelos 
#Pacientes
class Pacientes(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    sexo=models.CharField(max_length=35)
    edad = models.CharField(max_length=2)
    fechaNac = models.DateField(verbose_name='Fecha de Nacimiento')
    direccion = models.CharField(max_length=35)
    lugarNac = models.CharField(max_length=35)
    def __str__(self):
        texto = "{0} {1} ({2})"
        return texto.format(self.nombre, self.apellido, self.cedula)
class Meta:
    db_table = 'paciente'
    verbose_name = 'Paciente'
    verbose_name_plural = 'Pacientes'
    ordering = ['nombre']

######################################################################################

#Proveedores
class Proveedores(models.Model):
    cedula_prov = models.CharField(primary_key=True, max_length=10)
    rif = models.CharField(max_length=30)
    nombre_prov = models.CharField(max_length=35)
    apellido_prov = models.CharField(max_length=35)
    direccion_prov = models.CharField(max_length=35)
    telefono_prov = models.CharField(max_length=35)
    def __str__(self):
        texto = "{0} {1} ({2})"
        return texto.format(self.nombre_prov, self.apellido_prov, self.cedula_prov)
class Meta:
    db_table = 'proveedor'
    verbose_name = 'Proveedor'
    verbose_name_plural = 'Proveedores'
    ordering = ['nombre_prov']
#######################################################################################

    #Productos
class Productos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    nombrep = models.CharField(max_length=35)
    cantidad = models.CharField(max_length=35)
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombrep, self.codigo)
class Meta:
    db_table = 'producto'
    verbose_name = 'Producto'
    verbose_name_plural = 'Productos'
    ordering = ['nombrep']
###################################################################################

#Exámenes
class Examenes(models.Model):
    id_examenes = models.CharField(primary_key=True, max_length=10)
    nombre_examen = models.CharField(max_length=35)
    paciente = models.ForeignKey(Pacientes, null=True, blank=True, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        texto = "{0})"
        return texto.format(self.nombre_examen)
class Meta:
    db_table = 'examen'
    verbose_name = 'Examen'
    verbose_name_plural = 'Examenes'

####################################################################################



