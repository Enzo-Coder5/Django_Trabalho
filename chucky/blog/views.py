from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Post, Pessoa
from .forms import CustomUserCreationForm
from .forms import PessoaForm



@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')


def testing(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Bem-vindo, {user.username}!")

            
            try:
                pessoa = Pessoa.objects.get(usuario=user)

                if pessoa.tipo_usuario == "administrador":
                    return redirect("pagina_administrador")
                elif pessoa.tipo_usuario == "gerente":
                    return redirect("pagina_gerente")
                else:
                    return redirect("pagina_comum")

            except Pessoa.DoesNotExist:
                messages.warning(request, "Perfil de usuário não encontrado.")
                return redirect("home")

        else:
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, 'login.html')


def logout_view(request):
    auth_logout(request)
    messages.info(request, "Você saiu da sua conta.")
    return redirect('login')


def recuperar_senha(request):
    return render(request, 'recuperar_senha.html')


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Faça login.")
            return redirect("login")
        else:
            messages.error(request, "Erro ao criar conta. Verifique os dados.")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


@login_required(login_url='/login/')
def perfil(request):
    pessoa = Pessoa.objects.prefetch_related("enderecos").filter(usuario=request.user).first()
    if not pessoa:
        
        return redirect("home")
    return render(request, "perfil.html", {"pessoa": pessoa})




@login_required(login_url='/login/')
def lista_pessoas(request):
    pessoas = Pessoa.objects.select_related("usuario").prefetch_related("enderecos").all()
    return render(request, "pessoas/lista_pessoas.html", {"pessoas": pessoas})


@login_required(login_url='/login/')
def detalhe_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa.objects.prefetch_related("enderecos"), id=pessoa_id)
    return render(request, "pessoas/detalhe_pessoa.html", {"pessoa": pessoa})


def erro_403(request, exception=None):
    return HttpResponseForbidden("Acesso negado!")


def erro_500(request):
    raise Exception("Erro interno simulado")


@login_required(login_url='/login/')
def pagina_comum(request):
    pessoa = getattr(request.user, 'pessoa', None)
    if pessoa and pessoa.tipo_usuario == "comum":
        return render(request, "usuarios/comum.html")
    return HttpResponseForbidden("Acesso negado para este tipo de usuário.")

@login_required(login_url='/login/')
def pagina_administrador(request):
    pessoa = getattr(request.user, 'pessoa', None)
    if pessoa and pessoa.tipo_usuario == "administrador":
        return render(request, "usuarios/administrador.html")
    return HttpResponseForbidden("Acesso negado para este tipo de usuário.")

@login_required(login_url='/login/')
def pagina_gerente(request):
    pessoa = getattr(request.user, 'pessoa', None)
    if pessoa and pessoa.tipo_usuario == "gerente":
        return render(request, "usuarios/gerente.html")
    return HttpResponseForbidden("Acesso negado para este tipo de usuário.")

login_required(login_url='/login/')
def editar_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)

    if pessoa.usuario != request.user:
        return HttpResponseForbidden("Você não tem permissão para editar este perfil.")

    form = PessoaForm(request.POST or None, instance=pessoa)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Perfil atualizado com sucesso!")
        return redirect("perfil")

    return render(request, "pessoas/editar_pessoa.html", {"form": form})

@login_required(login_url='/login/')
def perfil(request):
    
    if request.user.is_superuser:
        return redirect("/admin/")

    pessoa = Pessoa.objects.filter(usuario=request.user).first()

    if not pessoa:
        messages.warning(request, "Seu perfil ainda não foi criado.")
        return redirect("home")

    return render(request, "perfil.html", {"pessoa": pessoa})


@login_required(login_url='/login/')
def perfil(request):
    
    if request.user.is_superuser:
        return redirect("/admin/")

    pessoa = Pessoa.objects.filter(usuario=request.user).first()

    if not pessoa:   
        pessoa = Pessoa.objects.create(
            usuario=request.user,
            nome=request.user.username,
            email=request.user.email,
            tipo_usuario="comum"
        )
        messages.info(request, "Seu perfil foi criado automaticamente.")

    return render(request, "perfil.html", {"pessoa": pessoa})


@login_required(login_url='/login/')
def editar_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    if pessoa.usuario != request.user:
        return HttpResponseForbidden("Você não tem permissão para editar este perfil.")
    form = PessoaForm(request.POST or None, instance=pessoa)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Perfil atualizado com sucesso!")
        return redirect("perfil") 
    return render(request, "pessoas/editar_pessoa.html", {"form": form})

@login_required(login_url='/login/')
def criar_pessoa(request):
    form = PessoaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        pessoa = form.save(commit=False)
        pessoa.usuario = request.user 
        pessoa.save()
        messages.success(request, "Pessoa criada com sucesso!")
        return redirect("lista_pessoas")
    return render(request, "pessoas/criar_pessoa.html", {"form": form})

@login_required(login_url='/login/')
def excluir_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    if pessoa.usuario != request.user:
        return HttpResponseForbidden("Você não tem permissão para excluir este perfil.")
    if request.method == "POST":
        pessoa.delete()
        messages.success(request, "Pessoa excluída com sucesso!")
        return redirect("lista_pessoas")
    return render(request, "pessoas/excluir_pessoa.html", {"pessoa": pessoa})


