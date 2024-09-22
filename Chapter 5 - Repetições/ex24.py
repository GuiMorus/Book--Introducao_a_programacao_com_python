# Modifique o programa anterior de forma a ler um número n. Imprima todos os primos até n

# Iniciando variáveis
div = 0
numeros = 1

# Introdução
print("-" * 10, "ATÉ O PRIMO", "-" * 10)

# Lendo número digitado pelo usuário
num = int(input("Digite o número: ").strip())

# Loop do programa principal
print(f"Os números primos são: ", end="")
while numeros <= num:

    # Verificando números primos
    for c in range(1, numeros + 1):

        # Div ganhando ponto caso o número for divisível pela range
        if numeros % c == 0:
            div += 1

    # Verificando se o número é primo
    if div == 2:
        print(f"{numeros} ", end="")

    # Ajustando variáveis de controle
    numeros += 1
    div = 0
