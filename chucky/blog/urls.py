from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('testing/', views.testing, name='testing'),

    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastrar/', views.register, name='register'),
    path('perfil/', views.perfil, name='perfil'),

    
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

    
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
    path('pessoas/<int:pessoa_id>/', views.detalhe_pessoa, name='detalhe_pessoa'),
    path('pessoas/<int:pessoa_id>/editar/', views.editar_pessoa, name='editar_pessoa'),


    
    path('forcar-403/', views.erro_403, name='forcar_403'),
    path('forcar-500/', views.erro_500, name='forcar_500'),

    
    path('comum/', views.pagina_comum, name='pagina_comum'),
    path('admin/', views.pagina_administrador, name='pagina_administrador'),
    path('gerente/', views.pagina_gerente, name='pagina_gerente'),
    
    path('pessoas/<int:pessoa_id>/excluir/', views.excluir_pessoa, name='excluir_pessoa'),

]
