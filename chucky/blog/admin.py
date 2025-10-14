from django.contrib import admin
from .models import Post, Pessoa, Endereco


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "data_criacao")
    search_fields = ("titulo",)



class EnderecoInline(admin.TabularInline):
    model = Endereco
    extra = 1


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "email", "telefone", "data_nascimento", "mostrar_bairros")
    search_fields = ("nome", "cpf", "email")
    list_filter = ("data_nascimento",)
    inlines = [EnderecoInline]

    def mostrar_bairros(self, obj):
        return ", ".join([end.bairro for end in obj.enderecos.all()])
    mostrar_bairros.short_description = "Bairros"


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ("rua", "numero", "bairro", "cidade", "estado", "cep", "pessoa")
    search_fields = ("rua", "bairro", "cidade", "estado", "cep")
    list_filter = ("cidade", "estado")
