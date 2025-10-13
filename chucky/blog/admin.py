from django.contrib import admin
from .models import Post, Pessoa


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "data_criacao")
    search_fields = ("titulo",)


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "email", "telefone", "data_nascimento", "bairro")
    search_fields = ("nome", "cpf", "email")
    list_filter = ("bairro", "data_nascimento")
