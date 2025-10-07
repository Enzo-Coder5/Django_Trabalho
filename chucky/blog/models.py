from django.db import models
from django.contrib.auth.models import User  
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Pessoa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
    nome = models.CharField(max_length=255, verbose_name='Nome')
    cpf = models.CharField(max_length=15, verbose_name='CPF')
    email = models.EmailField(verbose_name='Email')
    telefone = models.CharField(max_length=30, verbose_name='Telefone')
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    rg = models.CharField(max_length=30, verbose_name='RG', null=True, blank=True)
    endereco = models.CharField(max_length=255, verbose_name='Endereço residencial', null=True, blank=True)
    bairro = models.CharField(max_length=100, verbose_name='Bairro', null=True, blank=True)

    def __str__(self):
        return self.nome
