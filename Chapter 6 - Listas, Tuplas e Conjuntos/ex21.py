# Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
# os valores comuns às duas listas
# os valores que só existem na primeira
# os valores que existem apenas na segunda
# uma lista com os elementos não repetidos das suas listas
# a primeira lista sem os elementos repetidos na segunda

# Iniciando variáveis
listaA = {1, 2, 3, 4, 5, 10, 15, 23, 80}
listaB = {1, 2, 3, 4, 5, 0, 77, 66, 33}

# Introdução
print("-" * 10, "Teoria dos Conjuntos", "-" * 10)
print(f"Lista A: {listaA}")
print(f"Lista B: {listaB}")
print()

# Os valores comuns às duas listas
print("Valores comuns")
print(f"(Intersecção): {listaA & listaB}")
print()

# Os valores que só existem na primeira
print("Valores que existem somente na 1° Lista")
print(f"(Diferença de A para B): {listaA - listaB}")
print()

# Os valores que só existem na segunda
print("Valores que existem somente na 2° Lista")
print(f"(Diferença de B para A): {listaB - listaA}")
print()

# Elementos não repetidos das suas listas
print("Não repetidos nas 2 listas")
print(f"(União): {listaA | listaB}")
print()

# Elementos da 1° lista sem os elementos repetidos da 2° Lista
print("Elementos da 1° e da 2° sem repeti-los")
print(f"(Diferença de A para B: {listaA - listaB})")
