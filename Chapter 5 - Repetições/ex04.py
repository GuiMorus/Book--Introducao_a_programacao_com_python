# Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário,
# mas, dessa vez, apenas os números ímpares

# Lendo o último número digitado pelo usuário
fim = int(input("Digite o último número a imprimir: "))

# Repetição mostrando números ímpares
x = 1
while x < fim:
    print(x)
    x = x + 2

# Mostrando último número
print(fim)
