from django.db import models

# Modelos 
#Pacientes
class Pacientes(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    edad = models.CharField(max_length=2)
    
def __str__(self):
        texto = "{0} {1} ({2})"
        return texto.format(self.nombre, self.apellido, self.cedula)
    
    #Productos
class Productos(models.Model):
   codigo = models.CharField(primary_key=True, max_length=10)
   proveedor = models.CharField(max_length=35)
   nombrep = models.CharField(max_length=35)
   cantidad = models.CharField(max_length=35)
    
def __str__(self):
        texto = "{0} {1} ({2})"
        return texto.format(self.proveedor, self.nombre, self.cantidad)

#Proveedores
class Proveedores(models.Model):
   cedula = models.CharField(primary_key=True, max_length=10)
   nombre = models.CharField(max_length=35)
   apellido = models.CharField(max_length=35)
   ciudad = models.CharField(max_length=35)
    
def __str__(self):
        texto = "{0} {1} {2} ({3})"
        return texto.format(self.nombre, self.apellido, self.cedula, self.ciudad)
