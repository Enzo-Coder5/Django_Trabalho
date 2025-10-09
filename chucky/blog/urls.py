from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    # -------------------------
    # Páginas principais
    # -------------------------
    path('', views.home, name='home'),
    path('testing/', views.testing, name='testing'),

    # -------------------------
    # Autenticação
    # -------------------------
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # -------------------------
    # Recuperação de senha
    # -------------------------
    # Tela com botão (opcional)
    path('recuperar/', views.recuperar_senha, name='recuperar_senha'),

    # 1. Tela inicial para digitar o e-mail
    path('recuperar-senha/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        success_url=reverse_lazy('password_reset_done')
    ), name='password_reset'),

    # 2. Mensagem de confirmação de envio do e-mail
    path('recuperar-senha/enviado/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),

    # 3. Tela para redefinir a senha (link enviado por e-mail)
    path('recuperar-senha/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html',
        success_url=reverse_lazy('password_reset_complete')
    ), name='password_reset_confirm'),

    # 4. Mensagem final de sucesso após redefinir a senha
    path('recuperar-senha/concluido/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),
]
