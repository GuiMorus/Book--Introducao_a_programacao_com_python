# Criando uma tabela de preços em formato JSON

import json
from pathlib import Path

# Iniciando varável
tabela_de_preços = {}

# Texto inicial
print("Criador de tabela de preços")
print("Digite um nome de produto ou deixe em branco para terminar")

# Loop recolhendo nome dos produtos e seus preços
while produto := input("Nome do produto: ").strip().title():
    preço = input("Preço: ").strip().replace(',', '.')
    tabela_de_preços[produto] = preço

# Criando novo arquivo JSON com as informações da tabela
with Path("preços.json").open('w', encoding="utf-8") as arquivo:
    json.dump(tabela_de_preços, arquivo, indent=2, ensure_ascii=False)
