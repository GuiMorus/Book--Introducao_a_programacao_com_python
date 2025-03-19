# Escreva um programa que leia o nome do aluno e quatro notas.
# No final, o programa deve gravar os dados lidos em um arquivo em disco, usando
# o formato JSON

import json

# Iniciando variável
diretorio = './Arquivos de texto/notas.json'

# Recolhendo nome do usuário e suas notas
print("-" * 12, "Arquivador de notas", "-" * 12)

nome = input("Digite seu nome: ").strip().title()
nota1 = int(input("Digite sua 1° nota: ").strip())
nota2 = int(input("Digite sua 2° nota: ").strip())
nota3 = int(input("Digite sua 3° nota: ").strip())
nota4 = int(input("Digite sua 4° nota: ").strip())

# Calculando média
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"\nSua média é de: {media:.2f}\n")
print("Deseja arquivar a informação? [ S ] Sim - [ N ] Não")
escolha = input("Escolha: ").strip().upper()

# Verificando escolha
if escolha == 'S' or 'SIM':
    # Gerando dicionário
    cadastro = [{
        'nome': nome, 'nota1': nota1, 'nota2': nota2,
        'nota3': nota3, 'nota4': nota4, 'média': media
    }]

    # Criando arquivo JSON
    with open(diretorio, 'w', encoding='utf-8') as arquivo:
        # Convertendo dados do cadastro e montando o JSON dentro do arquivo
        json.dump(cadastro, arquivo, indent=2, ensure_ascii=False)

    # Mensagem de sucesso
    print("\033[32mInformações cadastradas com sucesso")
