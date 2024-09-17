# Escreva um programa que leia dois números. Imprima o resultado da multiplicação.
# Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se
# de que podemos entender a multiplicação de dois números como somas sucessivas de um
# deles. Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4

# Lendo números digitados pelo usuário
num1 = int(input("Digite o 1° fator: "))
num2 = int(input("Digite 0 2° fator: "))
resultado = 0

# Verificando maior número
if num1 > num2:
    c = num1    # contador

    # Repetição mostrando resultado
    while c > 0:
        resultado += num2
        print(resultado, end=" ")
        c -= 1
else:
    c = num1    # contador

    # Repetição mostrando resultado
    while c > 0:
        resultado += num2
        print(resultado, end=" ")
        c -= 1
