from django.contrib import admin
from .models import Servicio
# Register your models here.

class ServicioAdmin(admin.ModelAdmin): #incluir created and updated
    readonly_fields= ("created","updated")

admin.site.register(Servicio,ServicioAdmin) #registrar en el panel de administracion