from email.message import EmailMessage
from django.shortcuts import render, redirect
from .forms import formularioContacto
from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
#para guardar los datos del formulario
    formulario_contacto= formularioContacto()
    if request.method =="POST":
        formulario_contacto= formularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre= request.POST.get("nombre")
            email= request.POST.get("email")
            contenido= request.POST.get("contenido")

            #envio de email
            email=EmailMessage("Mensaje desde App Django",
            "El usuario {} con el c	orreo {} escribe: \n\n{}".format(nombre,email,contenido),
            "",["arnovisbuendiadeavila@gmail.com"])

            try:
                email.send()
                return redirect("/contacto/?valido")
            
            except:
                return redirect("/contacto/?novalido")

    return render(request,"ContactoApp/contacto.html",{"miformulario":formulario_contacto})