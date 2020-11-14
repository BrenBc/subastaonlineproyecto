from django.contrib import admin
from . models import Banco, Cliente, Proveedor, Tipotarjeta, Venta, Tarjeta, Puja
from . models import *

# Register your models here.

admin.site.register(Banco)
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Tipotarjeta)
admin.site.register(Venta)
admin.site.register(Tarjeta)
admin.site.register(Puja)
admin.site.register(Vehiculo)
admin.site.register(Fotografia)
admin.site.register(Categoria)