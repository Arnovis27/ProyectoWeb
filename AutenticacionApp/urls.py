from django.urls import path
from .views import VRegistro, cerrar_session,logear
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",VRegistro.as_view(),name="Autenticacion"), #una clase como vista
    path("cerrar/",cerrar_session,name="Cerrar"),
    path("logear/",logear,name="Logear"),
]