from django.shortcuts import render, redirect
from .models import Categoria

# Create your views here.
def home(request):
    categorias = Categoria.objects.all()
    return render(request, "index_categoria.html", {"categorias": categorias})


def salvar_categoria(request):
    name = request.POST.get("name")
    Categoria.objects.create(name=name)
    categorias = Categoria.objects.all()
    return render(request, "index_categoria.html", {"categorias": categorias})

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    return render(request, "editar_categoria.html", {"categoria": categoria})

def update_categoria(request, id):
    name = request.POST.get("name")
    categoria = Categoria.objects.get(id=id)
    categoria.name = name
    categoria.save()
    return redirect(home)

def deletar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect(home)