from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .models import *
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
  

def iniciosesion(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.info(request, 'El usuario o la contraseña es incorrecta')
            
    context = {}
    return render(request, 'usuario/login.html', context)

def cerrarsesion(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    tarjetas = Tarjeta.objects.all()
    ventas = Venta.objects.all()
    total_ventas = ventas.count()
    total_autos_comprados = Venta.objects.aggregate(Sum('precio'))
    clientes = Cliente.objects.all()



    contexto = {'tarjetas':tarjetas, 'ventas':ventas,
    'total_ventas':total_ventas, 'total_autos_comprados': total_autos_comprados,
    'clientes':clientes}
    return render(request, 'usuario/dashboard.html', contexto)



@login_required(login_url='login')
def usuario(request):
    vehiculos_lista = Vehiculo.objects.all()
    
    contexto = {'vehiculos_lista':vehiculos_lista}
    return render(request, 'usuario/usuario.html', contexto)
    
@login_required(login_url='login')
def subasta(request, pk):
    pujas = Puja.objects.all()
    vehiculos = Vehiculo.objects.all()
    vehiculo = Vehiculo.objects.get(id=pk)
        


    #return render(request, 'usuario/subasta.html')
    response = requests.get('https://apisubasta.herokuapp.com/api/vehiculo/').json()
    
    #for x in response:
        #id = x['id']
        
    
    #for x in response:
        #precio = x['precio']
        #pujas = precio + 200

    contexto = {'response':response, 'pujas': pujas, 'vehiculos': vehiculos,
    'vehiculo': vehiculo,}
    return render(request, 'usuario/subasta.html', contexto)

#def prueba(request):
    
