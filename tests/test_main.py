from src.main import buscar_pontos

DADOS_TESTE = [
    {"tipo": "Pilhas", "regiao": "Lago Sul", "endereco": "Local A"},
    {"tipo": "Oleo", "regiao": "Taguatinga", "endereco": "Local B"}
]


def test_buscar_pontos_sucesso():
    resultado = buscar_pontos(DADOS_TESTE, "Pilhas", "Lago Sul")
    assert len(resultado) == 1
    assert resultado[0]['endereco'] == "Local A"


def test_buscar_pontos_material_inexistente():
    resultado = buscar_pontos(DADOS_TESTE, "Papel", "Lago Sul")
    assert len(resultado) == 0


def test_buscar_pontos_regiao_errada():
    resultado = buscar_pontos(DADOS_TESTE, "Pilhas", "Taguatinga")
    assert len(resultado) == 0


def test_buscar_pontos_ignore_case():
    resultado = buscar_pontos(DADOS_TESTE, "pilhas", "LAGO SUL")
    assert len(resultado) == 1
