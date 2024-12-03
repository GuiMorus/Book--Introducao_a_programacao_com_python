# Escreva um generator capaz de gerar uma sequência com o fatorial de 1 até n, em que n
# é passado como parâmetro para o gerador

# Generator como função
def fatorial(n):
    fator = 1
    for i in range(1, n + 1):
        fator *= i
        yield fator


# Mostrando resultado com o generator
sequencia = list(fatorial(50))
print(sequencia)