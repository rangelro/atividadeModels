from django.contrib import admin
from .models import Produto
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome','preco', 'quantidade', 'dataCriacao']
    search_fields = ['codigo','nome']
    list_filter = ['dataCriacao']
    ordering = ['-dataCriacao']

admin.site.register(Produto, ProdutoAdmin)
