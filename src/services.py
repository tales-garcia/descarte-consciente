import json
import os
from math import radians, sin, cos, sqrt, atan2
import requests
from geopy.geocoders import Nominatim


def carregar_dados():
    caminho_arquivo = os.path.join(os.path.dirname(__file__), '..', 'dados.json')
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def obter_endereco(cep):
    cep = cep.replace("-", "").strip()

    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    dados = resposta.json()

    if "erro" in dados:
        raise ValueError(f"CEP inválido: {cep}")

    endereco = f"{dados['logradouro']}, {dados['localidade']}, {dados['uf']}, Brasil"
    return endereco


def obter_coordenadas(endereco):
    geolocator = Nominatim(user_agent="geolocalizacao")
    location = geolocator.geocode(endereco)

    if not location:
        raise ValueError(f"Não foi possível determinar coordenadas do endereço: {endereco}")

    lat = float(location.latitude)
    lon = float(location.longitude)

    return lat, lon


def distancia_km(lat1, lon1, lat2, lon2):
    R = 6371

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def buscar_pontos(pontos, cep_usuario, tipo):
    endereco_usuario = obter_endereco(cep_usuario)
    print("Endereço do usuário determinado: " + endereco_usuario)
    lat_user, lon_user = obter_coordenadas(endereco_usuario)

    resultados = []

    for ponto in pontos:
        if ponto['tipo'].lower() == tipo.lower():
            try:
                endereco = obter_endereco(ponto["cep"])
                lat_ponto, lon_ponto = obter_coordenadas(endereco)

                dist = distancia_km(
                    lat_user,
                    lon_user,
                    lat_ponto,
                    lon_ponto
                )

                resultados.append({
                    "tipo": ponto["tipo"],
                    "cep": ponto["cep"],
                    "endereco": endereco,
                    "distancia": round(dist, 2)
                })

            except Exception as e:
                print(f"Erro ao processar CEP {ponto['cep']}: {e}")

    resultados.sort(key=lambda x: x["distancia"])

    return resultados[:3]
