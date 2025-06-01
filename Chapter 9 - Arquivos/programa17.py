# Criando uma tabela de preços em formato JSON

import json
from pathlib import Path

# Iniciando variável
preços = {}

#===== MAIN CODE =====#
# Criando tabela
print("Criador de tabela de preços")
print("Digite um nome de produto ou em branco para terminar")
while produto := input("Nome do produto: "):
    valor = input("Preço: ")
    preços[produto] = valor

# Criando arquivo JSON
with Path("preços.json").open("w", encoding="utf-8") as arquivo:
    json.dump(preços, arquivo, ensure_ascii=False)
