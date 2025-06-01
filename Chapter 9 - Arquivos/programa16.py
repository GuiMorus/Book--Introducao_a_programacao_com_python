# Abrindo um arquivo JSON e usando os dados
import json
from pathlib import Path

with Path("lista.json").open(encoding='utf-8') as arquivo:
    print(f"Caminho do arquivo: {arquivo}")
    turma = json.load(arquivo)
for aluno in turma:
    print("Nome: ", str(aluno["nome"]).title())
    print("Notas: ", aluno["notas"])
    print(f"Média: {sum(aluno['notas']) / len(aluno['notas']):.2f}")
    print()
