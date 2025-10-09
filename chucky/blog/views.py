from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import Post


# Página inicial simples
def home(request):
    return render(request, 'home.html')


# Exemplo de listagem de posts
def testing(request):
    posts = Post.objects.all().values()
    template = loader.get_template('home.html')
    context = {'posts': posts}
    return HttpResponse(template.render(context, request))


# Login usando autenticação do Django
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, 'login.html')


# Logout → redireciona para a tela de logout.html
def logout_view(request):
    auth_logout(request)
    return render(request, 'logout.html')


# Tela com botão para recuperação de senha
def recuperar_senha(request):
    return render(request, 'recuperar_senha.html')
