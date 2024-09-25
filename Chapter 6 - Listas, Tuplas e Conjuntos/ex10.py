# Modifique o programa do Exercício 6.9 de forma a pesqusar p e v em toda a lista
# e informando ao usuário a posição onde p e a posição onde v foram encontrados.
#
# (Gui Morus)OBS: Desta fez modificarei o programa da minha forma atendendo a
# demanda do exercício

# Iniciando variável
lista = [15, 7, 27, 39]

# Lendo número digitado pelo usuário
p = int(input("Digite o 1° número para procurá-lo: ").strip())
v = int(input("Digite o 2° número para procurá-lo: ").strip())
p_ok = v_ok = False

# Repetição lendo a lista
for i in lista:

    # Verificando o 1° número
    if i == p:
        print(f"O número {p} foi encontrado na posição: {lista.index(i)}")
        p_ok = True     # indicando que p foi encontrado

    # Verificando se o 1° não foi encontrado
    elif i == lista[-1] and not p_ok:
        print(f"O número {p} não foi encontrado")

    # Verificando o 2° número
    if i == v:
        print(f"O número {v} foi encontrado na posição: {lista.index(i)}")
        v_ok = True     # indicando que v foi encontrado

    # Verificando se o 2° não foi encontrado
    elif i == lista[-1] and not v_ok:
        print(f"O número {v} não foi encontrado")
