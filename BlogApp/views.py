from django.shortcuts import render
from BlogApp.models import Post,Categorias

# Create your views here.
def blog(request):
    posts= Post.objects.all()
    return render(request,"BlogApp/blog.html",{"posts":posts})

def categoria(request, categoria_id):
    categoria= Categorias.objects.get(id=categoria_id)
    posts= Post.objects.filter(categorias=categoria)
    return render(request,"BlogApp/categoria.html",{"categoria":categoria,"posts":posts})