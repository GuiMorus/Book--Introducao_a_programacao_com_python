# Escreva u mprograma que receba o nome de um arquivo pela linha de comando e que imprima
# todas as linhas desse arquivo

import sys

# Declarando variável
nome_do_arquivo = sys.argv[1]

# Abrindo arquivo com with
with open(nome_do_arquivo, 'r') as arquivo:
    # Repetição lendo linhas do arquivo
    for linha in arquivo.readlines():
        # Mostrando linha
        print(linha)


# OBS:
# Abra o cmd (prompt de comando) digite o caminho do diretório
# Ao estar dentro deste diretório escreva:
# python ex01.py frutas.txt
# ou
# python ex01.py números.txt
