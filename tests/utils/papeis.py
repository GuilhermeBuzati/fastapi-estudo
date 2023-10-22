def create_papel_valido():
    return {
        "id": 0,
        "nome": "string",
        "sigla": "PETR4",
        "cnpj": "string"
    }

def create_papel_invalido(campos_invalido=['sigla']):
    papel_invalido =  {
        "id": 0,
        "nome": "string",
        "sigla": "PETR4",
        "cnpj": "string"
    }

    if 'sigla' in campos_invalido:
        papel_invalido['sigla'] = 'AAAAA'

    return papel_invalido