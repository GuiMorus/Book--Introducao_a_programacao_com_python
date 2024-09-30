# Altere o Programa 6.11 de forma a imprimir o menor elemento da lista.

# Programa 6.11: Verificação do menor valor
lista = [1, 7, 2, 4]
minimo = lista[0]

for i in lista:
    if i < minimo:
        minimo = i

print(minimo)
