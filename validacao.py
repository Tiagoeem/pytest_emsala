def valida_cpf(cpf):
    
    if not isinstance(cpf, str):
        return False

    if not cpf.isdigit():
        return False

    if len(cpf) != 11:
        return False

    return True


def valida_idade(idade: int) -> bool:
    
    return False