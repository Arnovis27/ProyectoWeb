from tabnanny import verbose
from venv import create
from django.db import models
from django.contrib.auth import get_user_model
from TiendaApp.models import producto
from django.db.models import F, Sum, FloatField

User= get_user_model() #video 67


# Create your models here
class Pedido(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        db_table= 'pedidos'
        verbose_name= 'pedido'
        verbose_name_plural='pedidos'
        ordering=['id']


class LineaPedido(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    producto= models.ForeignKey(producto, on_delete=models.CASCADE)
    pedido= models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad= models.IntegerField(default=1)
    created_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cantidad} Unidades de {self.producto.nombre}'

    class Meta:
        db_table= 'Lineapedidos'
        verbose_name= 'Lineapedido'
        verbose_name_plural='Lineaspedidos'
        ordering=['id']