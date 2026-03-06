from django.shortcuts import render, redirect
from .models import Produto
from categorias.models import Categoria

# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    return render(request, "index_produto.html", {"produtos": produtos})

def salvar_produto(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    storage = request.POST.get("storage")
    category_id = request.POST.get("category_id")
    categoria = Categoria.objects.get(id=category_id)
    Produto.objects.create(name=name, price=price, storage=storage, category_id=categoria)
    produtos = Produto.objects.all()
    return render(request, "index_produto.html", {"produtos": produtos})

def editar_produto(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, "editar_produto.html", {"produto": produto})

def update_produto(request, id):
    name = request.POST.get("name")
    price = request.POST.get("price")
    storage = request.POST.get("storage")
    category_id = request.POST.get("category_id")
    categoria = Categoria.objects.get(id=category_id)
    produto = Produto.objects.get(id=id)
    produto.name = name
    produto.price = price
    produto.storage = storage
    produto.category_id = categoria
    produto.save()
    return redirect(home)

def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect(home)