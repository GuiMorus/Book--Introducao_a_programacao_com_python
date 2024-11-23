# Reescreva o programa 8.2 de forma a utilizar for em vez de while.

# Programa 8.2: Como não escrever uma função (MODIFICADO E CORRIGIDO)
def soma(L):
    total = 0
    x = 0
    for i in range(x, len(L)):
        total += L[i]

    return total


# Utilizando a função soma
lista = [1, 2, 3, 6]
print(soma(lista))
