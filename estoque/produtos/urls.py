from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.lista_Produtos,name='lista_Produtos'),
    path('produto/<int:id>/', views.detalhes_Produto,name='detalhes_Produto'),
    path('categorias/', views.lista_Categorias,name='lista_categorias'),
    path('fornecedores/', views.lista_Fornecedores,name='lista_Fornecedores'),
]
