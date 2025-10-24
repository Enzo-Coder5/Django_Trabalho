from django.core.exceptions import ValidationError
import re

def validar_cpf(valor):
    cpf = re.sub(r'[^0-9]', '', valor)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        raise ValidationError("CPF inválido.")
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            raise ValidationError("CPF inválido.")
    return valor

def validar_rg(valor):
    rg = re.sub(r'[^0-9]', '', valor)
    if len(rg) < 5 or len(rg) > 14:
        raise ValidationError("RG deve conter entre 5 e 14 dígitos.")
    return valor

def validar_cep(valor):
    if not re.match(r'^\d{5}-\d{3}$', valor):
        raise ValidationError("CEP deve estar no formato 00000-000.")
    return valor

def validar_telefone(valor):
    telefone = re.sub(r'[^0-9]', '', valor)
    if len(telefone) < 10:
        raise ValidationError("Telefone deve conter DDD e número (mínimo 10 dígitos).")
    return valor
