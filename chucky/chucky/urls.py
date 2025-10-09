from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls')),   # todas as rotas do app blog ficam na raiz
    path('admin/', admin.site.urls),
]
