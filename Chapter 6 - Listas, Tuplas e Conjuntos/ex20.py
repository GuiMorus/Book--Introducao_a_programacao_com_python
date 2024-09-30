# Escreva um programa que gere um dicionário, em que cada chave seja um caractere,
# e seu valor seja o número desse caractere encontrado em uma frase lida.

# Iniciando variável
dicionario = {}

# Lendo frase digitada pelo usuário
frase = input("Digite a frase: ").strip()

# Repetição montando dicionário
for letra in frase:
    if letra in dicionario.keys():
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1

# Mostrando resultado
for caracter, quantidade in sorted(dicionario.items()):
    if caracter == ' ':
        caracter = "ESPAÇOS"
    print(f"{caracter}: {quantidade}")
