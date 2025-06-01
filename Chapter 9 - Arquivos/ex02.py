# Reescreva um programa similar com o exercício anterior para receber mais dois parâmetros
# a linha de início e a de fim para impressão. O programa deve imprimir apenas as linhas
# entre esses dois valores (incluindo as linhas início e fim)

import sys

# Definindo variáveis
nome_arquivo = sys.argv[1]
inicio = int(sys.argv[2])
fim = int(sys.argv[3])

# Abrindo arquivo com with
with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
    # Repetição lendo linhas do arquivo
    for i, linha in enumerate(arquivo, start=1):
        # Verificando inicio da linha
        if i >= inicio:
            print(linha, end='')    # Mostrando linha

        # Parando programa
        if i == fim:
            break

