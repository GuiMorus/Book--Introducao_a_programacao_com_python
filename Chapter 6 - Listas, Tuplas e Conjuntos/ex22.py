# Escreva um programa que compare duas listas. Considere a primeira lista como a versão
# inicial e a segunda como a versão após alterações. Utilizando operações com conjuntos, seu
# programa deverá imprimir a lista de modificações entre essas duas versões, listando:
#
# Os elementos que não mudaram
# Os novos elementos
# Os elementos que foram removidos

# Iniciando variáveis
lista_original = {1, 3, 7, 9}
lista_nova = {0, 1, 2, 3, 4, 8, 9, 10}

# Mostrando as listas
print(lista_original)
print(lista_nova)

# Os elementos que não mudaram
print("Elementos que não mudaram")
print(f"Intersecção: {lista_original & lista_nova}")
print()

# Os novos elementos
print("Elementos novos na Lista Nova")
print(f"Diferença(B - A): {lista_nova - lista_original}")
print()

# Os elementos que foram removidos
print("Elementos que foram removidos")
print(f"Diferença(A - B): {lista_original - lista_nova}")
