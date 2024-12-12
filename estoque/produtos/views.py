from django.shortcuts import render

from .models import Produto, Categoria, Fornecedor

def lista_Produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def detalhes_Produto(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, 'detalhes_produto.html', {'produto': produto})

def lista_Categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})

def lista_Fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores.html', {'fornecedores': fornecedores})
