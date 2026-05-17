from unittest.mock import patch
from src.services import buscar_pontos


DADOS_TESTE = [
    {"tipo": "Pilhas", "cep": "71600-000"},
    {"tipo": "Oleo", "cep": "72000-000"},
    {"tipo": "Pilhas", "cep": "71600-001"}
]


def mock_obter_endereco(cep):
    enderecos = {
        "70000-000": "Endereço do Usuário, DF",
        "71600-000": "Endereço Longe, DF",
        "72000-000": "Endereço do Óleo, DF",
        "71600-001": "Endereço Perto, DF"
    }
    cep_limpo = cep.replace("-", "").strip()
    cep_formatado = f"{cep_limpo[:5]}-{cep_limpo[5:]}" if len(cep_limpo) == 8 else cep

    if cep_formatado in enderecos:
        return enderecos[cep_formatado]
    raise ValueError(f"CEP inválido: {cep}")


def mock_obter_coordenadas(endereco):
    coords = {
        "Endereço do Usuário, DF": (-15.80, -47.90),
        "Endereço Perto, DF": (-15.81, -47.91),
        "Endereço Longe, DF": (-15.90, -48.00),
        "Endereço do Óleo, DF": (-15.85, -47.95)
    }
    if endereco in coords:
        return coords[endereco]
    raise ValueError(f"Coordenadas não encontradas: {endereco}")


@patch("src.services.obter_coordenadas", side_effect=mock_obter_coordenadas)
@patch("src.services.obter_endereco", side_effect=mock_obter_endereco)
def test_buscar_pontos_sucesso(mock_endereco, mock_coords):
    resultado = buscar_pontos(DADOS_TESTE, "70000000", "Pilhas")

    assert len(resultado) == 2
    assert resultado[0]['cep'] == "71600-001"
    assert resultado[0]['endereco'] == "Endereço Perto, DF"
    assert resultado[1]['cep'] == "71600-000"
    assert resultado[1]['endereco'] == "Endereço Longe, DF"
    assert "distancia" in resultado[0]


@patch("src.services.obter_coordenadas", side_effect=mock_obter_coordenadas)
@patch("src.services.obter_endereco", side_effect=mock_obter_endereco)
def test_buscar_pontos_material_inexistente(mock_endereco, mock_coords):
    resultado = buscar_pontos(DADOS_TESTE, "70000000", "Papel")
    assert len(resultado) == 0


@patch("src.services.obter_coordenadas", side_effect=mock_obter_coordenadas)
@patch("src.services.obter_endereco", side_effect=mock_obter_endereco)
def test_buscar_pontos_ignore_case(mock_endereco, mock_coords):
    resultado = buscar_pontos(DADOS_TESTE, "70000000", "pILhAs")
    assert len(resultado) == 2


@patch("src.services.obter_coordenadas", side_effect=mock_obter_coordenadas)
@patch("src.services.obter_endereco")
def test_buscar_pontos_ignora_cep_invalido_na_base(mock_endereco, mock_coords):
    def mock_endereco_com_falha(cep):
        if "71600-000" in cep:
            raise ValueError("Erro de conexão na API de CEP")
        return mock_obter_endereco(cep)

    mock_endereco.side_effect = mock_endereco_com_falha

    resultado = buscar_pontos(DADOS_TESTE, "70000000", "Pilhas")

    assert len(resultado) == 1
    assert resultado[0]['cep'] == "71600-001"
