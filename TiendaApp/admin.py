from django.contrib import admin
from .models import categoriaprod,producto
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(categoriaprod,CategoriaAdmin)
admin.site.register(producto, ProductoAdmin)