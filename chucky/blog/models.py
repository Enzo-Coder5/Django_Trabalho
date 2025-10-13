from django.db import models
from django.contrib.auth.models import User  

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Pessoa(models.Model):
   
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="pessoa")

    nome = models.CharField(max_length=255, verbose_name='Nome')
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')  
    email = models.EmailField(unique=True, verbose_name='Email')
    telefone = models.CharField(max_length=30, verbose_name='Telefone', blank=True, null=True)
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    rg = models.CharField(max_length=20, unique=True, verbose_name='RG', blank=True, null=True)
    endereco = models.CharField(max_length=255, verbose_name='Endereço residencial', blank=True, null=True)
    bairro = models.CharField(max_length=100, verbose_name='Bairro', blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return f"{self.nome} - {self.cpf}"

from django.utils import timezone

criado_em = models.DateTimeField(default=timezone.now, verbose_name="Criado em")
