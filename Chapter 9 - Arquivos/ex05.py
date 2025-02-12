# Crie um programa que inverta a ordem das linhas do arquivo pareseimpares.txt. A primeira linha deve
# conter o maior número, e a última, o menor

# Gerando arquivo de números invertido
with open('Arquivos de texto/pareseimparesinvertido.txt', 'w') as arquivo_invertido:

    # Abrindo arquivo com os números pares e ímpares
    with open('Arquivos de texto/pareseimpares.txt', 'r') as arquivo:

        # Repetição colocando o conteúdo invertido
        for i in reversed(arquivo.readlines()):
            arquivo_invertido.write(i)
