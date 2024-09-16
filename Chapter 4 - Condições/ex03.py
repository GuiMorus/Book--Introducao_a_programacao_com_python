# Escreva um programa que leia 3 números e que imprima o maior e o menor

# Lendo números do usuário
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro: "))
num3 = int(input("Digite outro: "))

# Iniciando variáveis
maior = num1
menor = num2

# Verificando maiores e menores números
if menor > maior:
    maior = num2
    menor = num1

if num3 > maior:
    maior = num3

if num3 < menor:
    menor = num3

# Mostrando o maior e menor número
print(f"Maior: {maior}")
print(f"Menor: {menor}")
