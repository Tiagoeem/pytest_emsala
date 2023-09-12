import pytest
from ..validacao import valida_cpf, valida_idade

@pytest.mark.entrada_de_dados
def test_valida_cpf_valido():
    assert valida_cpf("33652827610") == True

