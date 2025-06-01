# Programa lendo um arquivo JSON
import json
from pathlib import Path

# Abrindo arquivo
with Path("dados.json").open() as arquivo:
    dados = json.load(arquivo)
print(dados["nome"])
print(dados["valores"])
