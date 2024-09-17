# Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo
# segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração
# para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de
# dois números como a quantidade de vezes que podemos retirar o dividor do dividendo.
# Logo, 20 / 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20

# Lendo números do usuário
dividendo = int(input("Digite o numerador: "))
divisor = int(input("Digite o denominador: "))
print(f"{dividendo} / {divisor} = ", end="")

# Repetição calculando quociente
q = 0   # contador e quociente
while dividendo >= divisor:
    q += 1
    dividendo -= divisor

# Descobrindo resto
resto = dividendo

# Mostrando o resultado da equação
print(f"{q}")
print(f"resto: {resto}")
