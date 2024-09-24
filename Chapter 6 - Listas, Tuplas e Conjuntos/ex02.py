# Faça um programa que leia duas listas e que gere uma terceira com os elementos das
# duas primeiras

# Introdução
print("-" * 15, "UM + UM = TRÊS", "-" * 16)
print("| VAMOS JUNTOS 2 LISTAS EM UMA TERCEIRA LISTA |")

# Iniciando variáveis
lista1 = []
lista2 = []

# Recolhendo informações para acrescentar nas listas
c = 0   # controlador
print("para sair digite: Sair\n")

# Primeira Lista
while True:
    item = input(f"Digite o {c + 1}° item da lista 1: ")

    # Saindo do loop
    if item == 'sair':
        print()     # pulando linha
        break

    # Tratando e adicionando item na lista 1
    item = int(item) if item.isnumeric() else item
    lista1.append(item)

    # Ajustando variável controladora
    c += 1

# Segunda lista
c = 0   # controlador

while True:
    item = input(f"Digite o {c + 1}° item da lista 2: ")

    # Saindo do loop
    if item.lower() == 'sair':
        print()     # pulando linha
        break

    # Tratando e adicionando item na lista 2
    item = int(item) if item.isnumeric() else item
    lista2.append(item)

    # Ajustando variável de controle
    c += 1

# Gerando terceira lista
lista3 = lista1[:] + lista2[:]

# Mostrando a nova lista
print("3° lista gerada:")
print(lista3)
