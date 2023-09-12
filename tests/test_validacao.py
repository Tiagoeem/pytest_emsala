import pytest
from ..validacao import valida_cpf, valida_idade

@pytest.mark.cpf
def test_valida_cpf_valido():
    assert valida_cpf("33652827610") == True

@pytest.mark.cpf
def test_valida_cpf_com_mais_de_11_digitos():
    assert valida_cpf("336528276100") == False

@pytest.mark.cpf
def test_valida_cpf_com_menos_de_11_digitos():
    assert valida_cpf("336528") == False

@pytest.mark.cpf
def test_valida_cpf_com_somente_numeros():
    assert valida_cpf("336528A7610") == False

@pytest.mark.cpf
def test_valida_cpf_aceita_somente_strings():
    assert valida_cpf(33652827610) == False

@pytest.mark.idade
def test_valida_idade_positiva():
    assert valida_idade(5) == True