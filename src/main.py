import json
import os


def carregar_dados():
    caminho_arquivo = os.path.join(os.path.dirname(__file__), '..', 'dados.json')
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def buscar_pontos(dados, tipo_material, regiao_busca):
    resultados = []
    for item in dados:
        if item['tipo'].lower() == tipo_material.lower() and item['regiao'].lower() == regiao_busca.lower():
            resultados.append(item)
    return resultados


def main():
    print("--- Localizador de Descarte Consciente ---")
    tipo = input("O que você deseja descartar? (ex: Eletronicos, Oleo, Pilhas): ")
    regiao = input("Qual a sua região? (ex: Plano Piloto, Taguatinga, Lago Sul): ")

    dados = carregar_dados()
    pontos = buscar_pontos(dados, tipo, regiao)

    if pontos:
        print("\nPontos de coleta encontrados:")
        for p in pontos:
            print(f"- {p['endereco']}")
    else:
        print("\nNenhum ponto de coleta encontrado para esse material na sua região.")


if __name__ == "__main__":
    main()
