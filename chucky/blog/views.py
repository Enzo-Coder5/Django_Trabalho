from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from .models import Post, Pessoa



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
            return redirect('home')
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Faça login.")
            return redirect("login")
        else:
            messages.error(request, "Erro ao criar conta. Verifique os dados.")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})



@login_required(login_url='/login/')
def perfil(request):
    return render(request, "perfil.html", {"user": request.user})



@login_required(login_url='/login/')
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, "pessoas/lista_pessoas.html", {"pessoas": pessoas})



@login_required(login_url='/login/')
def detalhe_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    return render(request, "pessoas/detalhe_pessoa.html", {"pessoa": pessoa})



def erro_403(request, exception=None):
    return HttpResponseForbidden("Acesso negado!")


def erro_500(request):
    
    raise Exception("Erro interno simulado")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

       
        print(f"Usuário digitado: {username}")
        print(f"Senha digitada: {password}")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Bem-vindo, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, 'login.html')
