from django.db import models
from django.db.models.constraints import UniqueConstraint
# Modelos 
#Pacientes
class Pacientes(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    sexo=models.CharField(max_length=10)
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
    constraints = [
            UniqueConstraint(fields=['cedula'], name='cedula')
        ]

######################################################################################

#Proveedores
class Proveedores(models.Model):
    cedula_prov = models.CharField(primary_key=True, max_length=10)
    rif = models.CharField(max_length=15)
    nombre_prov = models.CharField(max_length=20)
    apellido_prov = models.CharField(max_length=20)
    direccion_prov = models.CharField(max_length=35)
    telefono_prov = models.CharField(max_length=20)
    def __str__(self):
        texto = "{0} {1} ({2})"
        return texto.format(self.nombre_prov, self.apellido_prov, self.cedula_prov)
class Meta:
    db_table = 'proveedor'
    verbose_name = 'Proveedor'
    verbose_name_plural = 'Proveedores'
    ordering = ['nombre_prov']
    constraints = [
            UniqueConstraint(fields=['cedula_prov'], name='cedula_prov')
        ]

#######################################################################################

    #Productos
class Productos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=12)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    nombrep = models.CharField(max_length=20)
    cantidad = models.CharField(max_length=20)
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombrep, self.codigo)
class Meta:
    db_table = 'producto'
    verbose_name = 'Producto'
    verbose_name_plural = 'Productos'
    ordering = ['nombrep']
    constraints = [
            UniqueConstraint(fields=['codigo'], name='codigo')
        ]
###################################################################################

#Exámenes
class Examenes(models.Model):
    nro_examen= models.AutoField(primary_key=True)
    nombre_examen= models.CharField(max_length=20)
    fecha_examen= models.DateField(verbose_name='Fecha de Examen')
    paciente= models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    def __str__(self):
        texto = "{0})"
        return texto.format(self.nombre_examen)
class Meta:
    db_table = 'examen'
    verbose_name = 'Examen'
    verbose_name_plural = 'Examenes'


#1 HEMATOLOGIA
#class Hematologia(Examenes):
    # eritrocitos= models.CharField(max_length=20)
    #hematocrito= models.CharField(max_length=20)
    #hemoglobina= models.CharField(max_length=20)
    #leucocitos=  models.CharField(max_length=20)
    #plaquetas=  models.CharField(max_length=20)  
    #neutrofilos= models.CharField(max_length=20)
    #linfocitos=  models.CharField(max_length=20)
    #eosinofilos= models.CharField(max_length=20)
    #monocitos= models.CharField(max_length=20)

####################################################################################
