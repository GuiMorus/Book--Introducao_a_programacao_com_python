# Crie um programa que leia os arquivos pares.txt e impares.txt e que cria um só arquivo
# pareseimpares.txt com todas as linhas dos outros dois arquivos, de forma a preservar a ordem numérica

# Gerando arquivo com números pares
with open('Arquivos de texto/pares.txt', 'w') as arquivo:
    # Repetição gerando números até 1000
    for i in range(0, 1001):
        # Verificando se o número é par
        if i % 2 == 0:
            arquivo.write(str(i) + '\n')

# Gerando arquivo com números ímpares
with open('Arquivos de texto/impares.txt', 'w') as arquivo:
    # Repetição gerando números até 1000
    for i in range(0, 1001):
        # Verificando se o número é ímpar
        if i % 2 != 0:
            arquivo.write(str(i) + '\n')

        # Correção de arquivo para o metodo zip() funcionar corretamente
        arquivo.write(' ') if i == 999 else None

# Gerando arquivo único com números dos arquivos de pares e ímpares
with open('Arquivos de texto/pareseimpares.txt', 'w') as arquivo:

    # Abrindo arquivos pares e impares
    with open('Arquivos de texto/pares.txt', 'r') as pares, open('Arquivos de texto/impares.txt', 'r') as impares:

        # Repetição inserindo os números pares e ímpares
        for i, n in zip(pares.readlines(), impares.readlines()):    # utilizando desempacotamento com zip
            arquivo.write(str(i))   # escrevendo par
            arquivo.write(str(n))   # escrevendo ímpar
