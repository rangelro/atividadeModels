from django.shortcuts import render,redirect

from .models import Produto, Categoria, Fornecedor
from .forms import CriarProduto

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

def produtoForm(request):
    if request.method == 'POST':
        form = CriarProduto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_Produtos')
    else:
        form = CriarProduto()
    return render(request, 'adicionar_produto.html', {'form': form})