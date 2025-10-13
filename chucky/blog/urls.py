from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('testing/', views.testing, name='testing'),

    
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        template_name='logout.html'
    ), name='logout'),

    
    path('recuperar/', views.recuperar_senha, name='recuperar_senha'),

    path('recuperar-senha/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        success_url=reverse_lazy('password_reset_done')
    ), name='password_reset'),

    path('recuperar-senha/enviado/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),

    path('recuperar-senha/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html',
        success_url=reverse_lazy('password_reset_complete')
    ), name='password_reset_confirm'),

    path('recuperar-senha/concluido/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),

    
    path('alterar-senha/', auth_views.PasswordChangeView.as_view(
        template_name='password_change.html',
        success_url=reverse_lazy('password_change_done')
    ), name='password_change'),

    path('alterar-senha/concluido/', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'
    ), name='password_change_done'),

    
    path('cadastrar/', views.register, name='register'),

    
    path('perfil/', views.perfil, name='perfil'),

    path('forcar-403/', views.erro_403, name='forcar_403'),

    path('forcar-500/', views.erro_500, name='forcar_500'),


]
