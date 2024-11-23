# Programa 8.13: Funções como parâmetro
def soma(a, b):
    return a + b


def subtração(a, b):
    return a - b


def imprime(a, b, parametro):
    print(parametro(4, 10))


imprime(5, 4, soma)

operacao = soma(5, 7)
