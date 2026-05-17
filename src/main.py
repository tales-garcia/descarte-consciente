from services import buscar_pontos, carregar_dados


def main():
    dados = carregar_dados()
    print("--- Localizador de Descarte Consciente ---")
    tipo = input("O que você deseja descartar? (ex: Eletronicos, Oleo, Pilhas): ")
    cep = input("Qual o seu CEP?: ")

    pontos = buscar_pontos(dados, cep, tipo)

    if pontos:
        print("\nPontos de coleta mais próximos:")
        for p in pontos:
            print(f"- {p['endereco']}: distância de {p['distancia']}km")
    else:
        print("\nNenhum ponto de coleta encontrado para esse material na sua região.")


if __name__ == "__main__":
    main()
