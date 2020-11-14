from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Tipotarjeta(models.Model):
    tipo_tarjeta= models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.tipo_tarjeta

class Banco(models.Model):
    nombrebanco = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nombrebanco

class Cliente(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE )
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, null=True)
    dpi = models.CharField(max_length=20, null=True)
    telefono= models.CharField(max_length=50, null=True)
    correoelectronico= models.EmailField(max_length=50, null=True)
    direccion= models.CharField(max_length=100, null=True)

    def __str__(self):
      
        return '%s %s' % (self.nombre, self.apellido)
        
        

class Tarjeta(models.Model):
    numerotarjeta= models.CharField(max_length=50)
    fecha_vencimiento= models.DateField()
    saldo_disponible = models.FloatField()
    tipotarjeta = models.ForeignKey(Tipotarjeta, related_name='tarj', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, related_name='client', on_delete= models.CASCADE)
    banco = models.ForeignKey(Banco, related_name='bank', on_delete = models.CASCADE)

    def __str__(self):
        return self.numerotarjeta

class Proveedor(models.Model):
    nombreproveedor = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreproveedor

class Puja(models.Model):
    Puja = models.IntegerField()
    fecha = models.DateTimeField()
    vehiculo = models.CharField(max_length=50, null=True)
    proveedor = models.ForeignKey(Proveedor, related_name='prov', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, related_name='cli', on_delete=models.CASCADE)

    
class Venta(models.Model):
    precio = models.FloatField()
    fecha_inicio= models.DateTimeField()
    fecha_fin= models.DateTimeField()
    vehiculo = models.CharField(max_length=50, null=True)
    proveedor = models.ForeignKey(Proveedor, related_name='proveed', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, related_name='clien', on_delete=models.CASCADE)
    



class Categoria(models.Model):
    tipo_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_categoria



class Vehiculo(models.Model):
    marca = models.CharField(max_length= 50)
    color = models.CharField(max_length= 50)
    kilometraje = models.IntegerField()
    precio = models.FloatField()
    combustible_vehiculo = models.CharField(max_length= 50, null=True)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE )
    estado_vehiculo = models.CharField(max_length= 50, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    puja = models.FloatField( null=True)

    def __str__(self):
        return '%s' % (self.marca)

    def pujar(self):
        resultado= self.precio + self.puja
        return resultado   

class Fotografia(models.Model):
    Fotografia = models.ImageField(blank=True )
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)

    def __str__(self):
        return self.fotografia.url




