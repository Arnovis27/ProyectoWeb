from distutils.command.upload import upload
from tkinter import image_names
from django.db import models

# Create your models here.

class categoriaprod(models.Model):
    nombre=models.CharField(max_length=50)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= "categoriaprod"
        verbose_name_plural="categoriasprod"

    def __str__(self):
        return self.nombre

class producto(models.Model):
    nombre= models.CharField(max_length=50)
    categorias= models.ForeignKey(categoriaprod,on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to="tienda",null=True, blank= True)
    precio= models.FloatField() 
    disponibilidad= models.BooleanField(default=True)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name="producto"
        verbose_name_plural="productos"

    def __str__(self):
        return self.nombre