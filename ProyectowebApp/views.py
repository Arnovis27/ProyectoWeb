from django.shortcuts import render
from django.http import HttpResponse

from carroApp.carro import Carro


# Create your views here.

def home(request):
    carro= Carro(request) #iniciar carro desde el inicio para evitar errores posteriores
    return render(request,"ProyectowebApp/home.html")
    