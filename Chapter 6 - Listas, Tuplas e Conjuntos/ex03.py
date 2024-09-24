# Faça um programa que percorra duas listas e gere uma terceira lista sem elementos repetidos

# Iniciando variáveis
lista1 = [4, 5, 7, 8, 10, 12, 11]
lista2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista3 = lista1[:]

# Repetição verificando lista
for i in lista2:
    # Contando quantidade do mesmo item dentro da lista
    item = lista3.count(i)

    # Verificando se há o item dentro da lista
    if item == 0:
        lista3.append(i)

# Mostrando as listas
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3: {lista3}")

lista3.sort()   # Ordenando lista
print(f"Lista 3 ordenada: {lista3}")

