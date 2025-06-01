# Crie um programa que imprima as linhas de um arquivo. Esse programa deve receber
# três parâmetros pela linha de comando: o nome do arquivo, a linha inicial e
# a última linha a imprimir

import sys

# Iniciando variáveis
nome_arquivo = str(sys.argv[1])
inicio = int(sys.argv[2])
fim = int(sys.argv[3])

# Filtrando nome do arquivo
if not nome_arquivo.endswith('.txt'):

    nome_arquivo = f"{nome_arquivo}.txt"    # Corrigindo nome do arquivo

# Abrindo arquivo
with open(nome_arquivo, encoding='utf-8') as arquivo:

    # Iniciando contador
    cont = 1

    # Repetição lendo cada linha do arquivo
    for linha in arquivo.readlines():

        # Verificando se o contador entá dentro do limite
        if cont in range(inicio, fim + 1):

            # Mostrando linhas do arquivo
            print(linha, end="")

        # Incrementando contador
        cont += 1
