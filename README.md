# Localizador de Descarte Consciente

## Descrição do Problema
O descarte irregular de materiais como pilhas, baterias, lixo eletrônico e óleo de cozinha é um problema ambiental recorrente. Muitas pessoas têm a intenção de descartar corretamente, mas não sabem onde encontrar os pontos de coleta adequados em suas regiões.

## Proposta da Solução
Uma aplicação simples de interface de linha de comando (CLI) que permite ao usuário informar o tipo de material que deseja descartar e a sua região. O sistema retorna os endereços dos pontos de coleta mais próximos.

## Público-Alvo
Cidadãos comuns que buscam informações rápidas e práticas sobre locais para descarte sustentável de resíduos domiciliares.

## Funcionalidades Principais
- Busca de pontos de coleta por tipo de material.
- Filtragem de pontos de coleta por região.
- Exibição formatada dos endereços encontrados.

## Tecnologias Utilizadas
- Python 3.10+
- pytest
- flake8
- GitHub Actions

## Instruções de Instalação

```bash
git clone http://github.com/tales-garcia/
cd descarte-consciente
python -m venv venv_dev
venv_dev\Scripts\activate
pip install -r requirements.txt
```
## Instruções de Execução
```bash
python src/main.py
```
## Instruções para Rodar os Testes
```bash
python -m pytest
```
## Instruções para Rodar o Lint
```bash
flake8 src/ tests/
```
## Versão Atual
`1.0.0`
## Autor
Tales Pessoa Garcia