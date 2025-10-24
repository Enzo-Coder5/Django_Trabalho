from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Pessoa


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="E-mail",
        widget=forms.EmailInput(attrs={"placeholder": "Digite seu e-mail"})
    )

    tipo_usuario = forms.ChoiceField(
        choices=[
            ("comum", "Comum"),
            ("administrador", "Administrador"),
            ("gerente", "Gerente")
        ],
        label="Tipo de Usuário",
        required=True
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso. Escolha outro.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            Pessoa.objects.create(
                usuario=user,
                nome=user.username,
                email=user.email,
                tipo_usuario=self.cleaned_data["tipo_usuario"],
                cpf="000.000.000-00",
                rg="0000000",
                telefone="",
                data_nascimento="2000-01-01"
            )
        return user


class PessoaForm(forms.ModelForm):
    tipo_usuario = forms.ChoiceField(
        choices=[
            ("comum", "Comum"),
            ("administrador", "Administrador"),
            ("gerente", "Gerente")
        ],
        label="Tipo de Usuário",
        required=True
    )

    class Meta:
        model = Pessoa
        fields = ["nome", "cpf", "rg", "email", "telefone", "data_nascimento", "tipo_usuario"]
        widgets = {
            "data_nascimento": forms.DateInput(attrs={"type": "date"})
        }