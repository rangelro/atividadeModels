from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    codigo = models.CharField(max_length=100, unique=True,null=False, blank=False)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    dataCriacao = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.nome


