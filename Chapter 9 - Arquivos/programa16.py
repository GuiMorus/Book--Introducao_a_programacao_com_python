# Abrindo arquivo JSON e usando os dados

import json
from pathlib import Path

# Abrindo arquivo
with Path("lista.json").open(encoding='utf-8') as arquivo:
    turma = json.load(arquivo)

for aluno in turma:
    print(f"Nome: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {sum(aluno['notas']) / len(aluno['notas'])}")
    print()
