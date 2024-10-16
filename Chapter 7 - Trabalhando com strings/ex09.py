# Modifique o jogo da forca (Programa 7.2) de forma a escrever a palavra secreta
# caso o jogador perca.

# Programa 7.2: Jogo da forca
# Comentado e modificado

# Iniciando variável
perdeu = True

# Introdução
print("*--" * 5, "JOGO DA FORCA 😜", "--*" * 5)

# Loop do programa principal(jogo)
while True:
    # Verificando status do jogo
    if perdeu:
        # Lendo palavra escolhida pelo usuário
        palavra = input("Digite a palavra secreta: ").lower().strip()

        # Iniciando variáveis
        digitadas = []
        acertos = []
        erros = 0
        perdeu = False

        # Repetição gerando espaçamento
        for c in range(50):
            print()

    senha = ""      # Gerando texto oculto

    # Repetição escrevendo a senha
    for letra in palavra:
        senha += letra if letra in acertos else "."

    # Mostrando a palavra oculta
    print(senha)

    # Verificando vitória
    if senha == palavra:
        print("Você acertou")
        break

    # Lendo tentativa do jogador
    tentativa = input("\nDigite uma letra: ").lower().strip()

    # Verificando se jogador já escolheu a letra
    if tentativa in digitadas:
        print("Você já tentou essa letra!")
        continue
    else:
        digitadas += tentativa      # tentativa entra na lista das letras digitadas

        # Verificando acerto ou erro da tentativa
        if tentativa in palavra:
            acertos += tentativa    # tentativa entra na lista de acertos
        else:
            erros += 1
            print("Você errou!")

    # Desenhando forca
    print("X==:==\nX    :   ")                  # Topo da forca
    print("X    😐   " if erros >= 1 else "X")   # boneco(cabeça) da forca

    # Verificando erros para desenhar o boneco(corpo)
    linha2 = ""                                 # boneco(corpo) da forca
    if erros == 2:
        linha2 = "    |   "                     # boneco(tronco) da forca
    elif erros == 3:
        linha2 = "   \|   "                     # boneco(L. Braço) da forca
    elif erros >= 4:
        linha2 = "   \|/  "                     # boneco(R. Braço) da forca

    print(f"X{linha2}")                         # mostrando corpo do boneco

    # Verificando erros para desenhar o boneco(pernas)
    linha3 = ""                                 # boneco(pernas) da forca
    if erros == 5:
        linha3 += "   /  "                      # boneco(L. Perna) da forca
    elif erros >= 6:
        linha3 += "   / \ "                     # boneco(R. Perna) da forca

    print(f"X{linha3}")                         # mostrando perna do boneco
    print("X\n===========")

    # Verificando erro máximo
    if erros == 6:
        print("Enforcado!")
        perdeu = True
        continue
