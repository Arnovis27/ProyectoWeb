from django.shortcuts import redirect,render
from TiendaApp.models import producto
from .carro import Carro
# Create your views here.

def agregar_producto(request,producto_id):
    carro= Carro(request)
    produc= producto.objects.get(id=producto_id)
    carro.agregar(producto=produc)
    return redirect("Tienda")

def eliminar_producto(request,producto_id):
    carro= Carro(request)
    produc= producto.objects.get(id=producto_id)
    carro.eliminar(producto=produc)
    return redirect("Tienda")

def restar_producto(request,producto_id):
    carro= Carro(request)
    produc= producto.objects.get(id=producto_id)
    carro.restar_producto(producto=produc)
    return redirect("Tienda")

def limpiar_carro(request,producto_id):
    carro= Carro(request)
    carro.limpiar_carro()
    return redirect("Tienda")