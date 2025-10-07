from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User


def home(request):
    return HttpResponse("<h1>Bem-vindo ao Blog!</h1>")


def home(request):
    return render(request, 'home.html')




def testing(request):
  posts = Post.objects.all().values()
  template = loader.get_template('home.html')
  context = {
    'posts': posts,
  }
  return HttpResponse(template.render(context, request))



def login(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        senha = request.POST.get("senha")
        posts = Post.objects.all().values()
        print(nome)
        print(senha)
        return render(request, 'home.html', locals())

    return render(request, 'login.html', locals())


from .models import Pessoa



def login(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        senha = request.POST.get("senha")
        lista_pessoas = []
        pessoas = Pessoa.objects.all().values()
        for i in pessoas:
            p_json = {}
            p_json['id'] = i['id']
            p_json['usuario_id'] = i['usuario_id']
            p_json['data_nascimento'] = i['data_nascimento']
            usuario = User.objects.get(id=i['usuario_id'])
            p_json['name_usuario'] = usuario.username
            p_json['primeir_nome_usuario'] = usuario.first_name
            p_json['email_usuario'] = usuario.email
            lista_pessoas.append(p_json)


        pessoas = lista_pessoas

        return render(request, 'home.html', locals())

    return render(request, 'login.html', locals())

from django.contrib.auth import logout
from django.shortcuts import render

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')