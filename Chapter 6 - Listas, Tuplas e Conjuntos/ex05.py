# Altere o Programa 6.7 de forma a poder trabalhar com vários comandos digitados
# de uma só vez. Atualmente, apenas um comando pode ser inserido por vez.
# Altere-o de forma a considerar operações como uma string.
#
# Exemplo: FFFAAAS significaria 3 chegadas de novos clientes, 3 atendimentos e, finalmente,
# a saída do programa.

# Programa 6.7: Simulação de uma fila de banco
ultimo = 10
fila = list(range(1, ultimo + 1))
ativo = True

while ativo:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite as seguintes operações:")
    print("[ F ] - para adicionar um cliente ao final da fila.")
    print("[ A ] - para realizar o atendimento.")
    print("[ S ] - para sair do programa")

    # Lendo opção selecionada
    operação = input("Operação: ").strip().upper()

    # Repetição das operações escolhidas
    for i in range(0, len(operação)):

        # Variável recebendo a primeira operação digitada
        atual = operação[0]

        # Verificando atendimento
        if atual == "A":

            # Verificando se há cliente na fila
            if len(fila) > 0:

                # Retirando o primeiro cliente da fila
                atendimento = fila.pop(0)
                print(f"Cliente {atendimento} atendido")
            else:
                print("Fila vazia! Ninguém para atender")

        # Verificando adicionamento de cliente
        elif atual == "F":
            ultimo += 1     # Incrementa o ticket do novo cliente
            fila.append(ultimo)     # Adicionando cliente na fila
            print(f"O cliente {ultimo} foi adicionado a fila")

        # Verificando saida do programa
        elif atual == "S":
            ativo = False
            break

        # Verificando se há opção inválida
        else:
            print("Operação inválida! Digite apenas F, A ou S!")

        # Removendo opção atual
        operação = operação.removeprefix(atual)
