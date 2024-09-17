# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
# Exiba o resultado da operação solicitada.

# Introdução
print("+-x÷" * 3, "--- SIMPLULADORA ---", "+-x÷" * 3)

# Lendo números do usuário
num1 = float(input("Primeiro número: ").strip().replace(',', '.'))
num2 = float(input("Segundo número: ").strip().replace(',', '.'))

# Verificando opção desejada
print()     # pulando linha
print("-" * 20)
print("SELECIONE A CONTA DESEJADA")
print("[ 1 ] Somar        [ 3 ] Multiplicar")
print("[ 2 ] Subtrair     [ 4 ] Dividir")

opção = int(input("Opção: "))

# Realizando conta dependendo da opção
if opção == 1:
    print(f"{num1} + {num2} = {num1 + num2}")

elif opção == 2:
    print(f"{num1} - {num2} = {num1 - num2}")

elif opção == 3:
    print(f"{num1} x {num2} = {num1 * num2}")
elif opção == 4:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE")
