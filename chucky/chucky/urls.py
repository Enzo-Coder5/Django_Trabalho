from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler403, handler500

urlpatterns = [
    path('admin/', admin.site.urls),         
    path('', include('blog.urls')),         
]


handler403 = 'blog.views.erro_403'
handler500 = 'blog.views.erro_500'
