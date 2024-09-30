# Modifique o Programa 6.13 de forma a mostrar quantos ingressos foram vendidos em cada sala.
# Utilize uma lista do mesmo tamanho da quantidade de salar e utilize seus elementos para contar
# quantos ingressos foram vendidos em cada sala. Imprima na tela o total das vendas
# no fim do programa

# Programa 6.13: Controle da utilização de salas de um cinema

# Iniciando variáveis
lugares_vagos = [10, 2, 1, 3, 0]
vendidos = [0, 0, 0, 0, 0]

# Loop do programa principal
while True:
    # Recolhendo número da sala
    print("\nDigite 0 para sair")
    sala = int(input("Sala: "))

    # Verificando saída
    if sala == 0:
        print("FIM")
        break

    # Verificando se sala existe
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida")

    # Verificando se há vagas
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")

    else:
        # Recolhendo quantidade de vagas definidas pelo usuário
        lugares = int(input(f"Quantos lugares deseja ({lugares_vagos[sala - 1]} vagos): ").strip())

        # Verificando se vagas solicitadas excede o límite
        if lugares > lugares_vagos[sala - 1]:
            print("Número de lugares indisponível")

        # Verificando se vagas é menor que 0
        elif lugares < 0:
            print("Número de vagas inválido")

        else:
            # Ajustando lista com as vagas
            lugares_vagos[sala - 1] -= lugares

            # Ajustando quantidade de ingressos vendidos
            vendidos[sala - 1] = lugares
            print(f"{lugares} lugares vendidos")

# Mostrando resultado final
print(" Utilização das salas")
for sala, vagos in enumerate(lugares_vagos):
    print(f"Sala {sala + 1} --- {vagos} lugar(es) vazio(s) || {vendidos[sala]} ingressos vendidos")

