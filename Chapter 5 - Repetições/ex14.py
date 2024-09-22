# Escreva um programa que leia números inteiros do teclado. O programa deve ler os
# números até que o usuário digite 0. No final da execução, exiba a quantidade de números
# digitados, assim como a soma e a média aritmética.

# Introdução
print("-" * 10, "SOMA, SOMA A SOMA", "-" * 10)

# Iniciando variáveis
c = 0   # contador
soma = 0

# Repetição recolhendo números
while True:
    numero = int(input("Digite um número inteiro: ").strip())

    # Verificando saída
    if numero == 0:
        break

    # Somando e administrando contador
    soma += numero
    c += 1

# Mostrando informações
media = soma / c

print(f"\nVocê digitou {c} números")
print(f"A soma entre eles: {soma}")
print(f"A média aritmética: {media:.2f}")
