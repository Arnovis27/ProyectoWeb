from django.urls import path
from pedidos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.procesar_pedido,name="procesar_pedido"),
]