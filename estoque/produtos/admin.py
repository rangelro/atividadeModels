from django.contrib import admin
from .models import *
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome','preco', 'quantidade', 'dataCriacao']
    search_fields = ['codigo','nome']
    list_filter = ['dataCriacao']
    ordering = ['-dataCriacao']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome','descricao']
    search_fields = ['nome']

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['nome','cnpj']
    search_fields = ['nome']

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
