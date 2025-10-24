from django.db import models
from django.contrib.auth.models import User
from .validators import validar_cpf  


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Pessoa(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('comum', 'Comum'),
        ('gerente', 'Gerente'),
        ('administrador', 'Administrador'),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="pessoas"
    )

    nome = models.CharField(max_length=255, verbose_name='Nome')
    cpf = models.CharField(
        max_length=14,
        unique=True,
        verbose_name='CPF',
        validators=[validar_cpf]
    )
    email = models.EmailField(unique=True, verbose_name='Email')
    telefone = models.CharField(max_length=30, verbose_name='Telefone', blank=True, null=True)
    data_nascimento = models.DateField(verbose_name='Data de nascimento', null=True, blank=True)
    rg = models.CharField(max_length=20, unique=True, verbose_name='RG', blank=True, null=True)

    tipo_usuario = models.CharField( 
        max_length=20,
        choices=TIPO_USUARIO_CHOICES,
        default='comum',
        verbose_name='Tipo de usuário'
    )

    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.cpf}"


class Endereco(models.Model):
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name="enderecos"
    )
    rua = models.CharField(max_length=255, verbose_name="Rua")
    numero = models.CharField(max_length=10, verbose_name="Número")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    estado = models.CharField(max_length=2, verbose_name="Estado") 
    cep = models.CharField(max_length=9, verbose_name="CEP")

    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
        ordering = ["cidade", "bairro"]

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado}"