# Validador de Entrada de Dados

Neste exercício, você irá implementar e testar funções para validar entradas comuns em sistemas: CPF e idade.

## Requisitos:

### Função de Validação de CPF (`valida_cpf`):

- A entrada é uma string representando um CPF.
- O CPF deve ter exatamente 11 dígitos.
- A função deve retornar `True` se o CPF for válido e `False` caso contrário.
- Se o CPF tiver mais de 11 dígitos ou menos de 11 dígitos, a função deve retornar `False`.
- Se o CPF contiver caracteres não numéricos, a função deve retornar `False`.

### Função de Validação de Idade (`valida_idade`):

- A entrada é um número inteiro representando a idade.
- A idade não pode ser negativa e nem maior que 120.
- A função deve retornar `True` se a idade for válida.
- Se a idade for negativa, a função deve lançar uma exceção com a mensagem "Idade não pode ser negativa".
- Se a idade for maior que 120, a função deve lançar uma exceção com a mensagem "Idade improvável".

## Testes:

Você deve escrever testes usando o `pytest` para garantir que suas funções estejam funcionando corretamente. Use o marcador `entrada_de_dados` para esses testes.
