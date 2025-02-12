# Crie um programa que receba o nome de dois arquivos como parâmetros da linha de comando (prompt)
# e que gere um arquivo de saída com as linhas do primeiro seguidas das linhas do segundo arquivo.
# O nome do arquivo de saída também pode ser passado como parâmetro na linha de comandos.
import string
import sys

# Iniciando variáveis
primero_arquivo = sys.argv[1]
segundo_arquivo = sys.argv[2]
saida_arquivo = sys.argv[3]

# Lista com as letras do alfabeto
letras = list(string.ascii_lowercase)

# Gerando arquivos para leitura do código
with open('Arquivos de texto/minusculos.txt', 'w') as minusculos, open('Arquivos de texto/maiusculos.txt', 'w') as maiusculos:

    # Repetição colocando as letras dentro dos seus respectivos arquivos
    for i in letras:
        minusculos.write(i + '\n')
        maiusculos.write(i.upper() + '\n')

# Gerando saida de arquivo lendo outros 2 arquivos
with open(primero_arquivo, 'r') as arquivo1, open(segundo_arquivo, 'r') as arquivo2:

    # Gerando arquivo de saida
    with open(saida_arquivo, 'w', encoding='utf-8') as saida:
        # Repetição inserindo o primeiro arquivo ao arquivo de saida
        for i in arquivo1.readlines():
            saida.write(i)

        # Repetição inserindo o segundo arquivo ao arquivo de saida
        for i in arquivo2.readlines():
            saida.write(i)
