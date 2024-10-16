# Escreva um jogo da velha para dois jogadores. O jogo deve perguntaqr onde você quer jogar
# e alterar entre os jogadores.

# Introdução
print("=" * 10, "JOGO DA VELHA", "=" * 10)

# Iniciando variáveis
linha1 = ['', '', '']
linha2 = ['', '', '']
linha3 = ['', '', '']
vitoria = ''
posição = []
jogador1 = True


def verificar_vitoria(simbolo):
    global vitoria  # definindo escopo global

    # Verificando vitória
    l1 = linha1.count(simbolo)
    l2 = linha2.count(simbolo)
    l3 = linha3.count(simbolo)

    # Verificação simples
    if l1 == 3 or l2 == 3 or l3 == 3:
        vitoria = simbolo
        return True

        # debug
        #print("Vitoria simples")

    # Verificação vertical
    for c in range(0, 3):
        if {linha1[c], linha2[c], linha3[c]} == {simbolo}:
            vitoria = simbolo
            return True

            # debug
            #print("Vitória vertical")

    # Verificação diagonal
    if {linha2[1], linha1[0], linha3[2]} == {simbolo}:
        vitoria = simbolo
        return True

        # debug
        #print("Vitoria Diagonal 1")

    elif {linha2[1], linha1[2], linha3[0]} == {simbolo}:
        vitoria = simbolo
        return True

        # debug
        #print("Vitoria Diagonal 2")

    # Não houve vitória
    return False


# --- PROGRAMA PRINCIPAL --- #
while vitoria == '':
    # -- Desenhando grade -- #
    print("\n")     # Pulando 2 linhas

    # Repetição atribuindo valores das linhas
    posição.clear()
    for i in linha1:
        posição.append(i)

    for i in linha2:
        posição.append(i)

    for i in linha3:
        posição.append(i)

    t = 0   # controlador do traço
    for c in range(1, 10):
        # Mostrando jogadas
        if posição[c - 1] == '':
            print(f" {c} ", end="")
        else:
            # Definindo cor de texti
            if posição[c - 1] == 'x':
                cor = "\033[32m"
            else:
                cor = "\033[34m"

            # Mostrando jogada em si
            print(f" {cor + str(posição[c - 1] + "\033[m")} ", end="")

        # Verificando contador para desenhar os traços
        if t < 2:
            print("|", end="")
            t += 1
        else:
            t = 0

        # Verificando multiplos de 3
        if c % 3 == 0:
            print()     # Quebrando linha a cada 3 numeros
            print("-" * 12)

    # -- Jogada dos jogadores -- #

    # Verificando vitória
    if verificar_vitoria("x") or verificar_vitoria("o"):
        print("🎉" * 13)
        print(f"🎈🎈🎈 VITÓRIA DE:  {vitoria}  🎈🎈🎈")
        exit()

    # Verificando empate
    if '' not in posição:
        print("Empate!!!")
        break

    # Recolhendo jogada
    print("Escolha uma posição")
    simbolo_jogo = "x" if jogador1 else "o"
    jogada = int(input(f"JOGADOR ( {simbolo_jogo} ): ").strip().lower())
    jogador1 = not jogador1

    # Atribuindo jogada
    mensagem = "Jogada inválida"

    match jogada:
        case 1:
            if linha1[0] == '':
                linha1[0] = simbolo_jogo
            else:
                print(mensagem)

        case 2:
            if linha1[1] == '':
                linha1[1] = simbolo_jogo
            else:
                print(mensagem)

        case 3:
            if linha1[2] == '':
                linha1[2] = simbolo_jogo
            else:
                print(mensagem)

        case 4:
            if linha2[0] == '':
                linha2[0] = simbolo_jogo
            else:
                print(mensagem)

        case 5:
            if linha2[1] == '':
                linha2[1] = simbolo_jogo
            else:
                print(mensagem)

        case 6:
            if linha2[2] == '':
                linha2[2] = simbolo_jogo
            else:
                print(mensagem)

        case 7:
            if linha3[0] == '':
                linha3[0] = simbolo_jogo
            else:
                print(mensagem)

        case 8:
            if linha3[1] == '':
                linha3[1] = simbolo_jogo
            else:
                print(mensagem)

        case 9:
            if linha3[2] == '':
                linha3[2] = simbolo_jogo
            else:
                print(mensagem)

