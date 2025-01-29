# Melhore o programa do exercício anterior perguntando ao jogador o nível de dificuldade desejado.
# MODO FÁCIL: vida começa com 100 e dano de 1 - 10
# MODO MÉDIO: vida começa com 80 e dano de 5 - 15
# MODO DIFÍCIL: vida começa com 65 e dano de 7 - 20
# MODO CARIOCA: vida começa com 50 e dano vai de 20 - 100

from random import randint
from time import sleep

# Iniciando variáveis
VIDA = 0
MODO = {"fácil": [100, 1, 10], "médio": [80, 5, 15], "difícil": [65, 7, 20], "carioca": [50, 20, 100]}
alien = randint(1, 100)
erros = []
fim = False

# Mensagem principal do jogo
print("🔫" * 8, "O alien👽 e as árvores🌳", "🔫" * 8)
print()
print("Um alienígena com uma arma está escondido atrás de uma árvore")
print("Cada árvore foi númerada de 1 a 100\n")

# Perguntando a dificuldade do jogo
print("MODOS:")
print("Fácil | Médio | Difícil | Carioca")
dificuldade = input("Escolhe a dificuldade do jogo: ").strip().lower()

# Definindo valores conforme a dificuldade
VIDA = MODO[dificuldade][0]
dano_minimo = MODO[dificuldade][1]
dano_maximo = MODO[dificuldade][2]

# Loop principal
while VIDA > 0:
    print("\nEncontre o alienígena antes que ele acabe com suas vidas")

    # Gerando árvores
    for c in range(1, 101):
        # Verificando tentativas do usuario
        if c in erros:
            print("❌", end="")      # aparece X caso o usuário escolhe este número

        elif fim and c == alien:
            print("👽", end="")      # aparece o alienígena caso usuário acerte

        else:
            print("🌳", end="")      # aparece a árvore onde o usuário não escolheu

        # Pulando linha a cada 20 árvores
        if c % 20 == 0:
            print()

    # Mostrando vida atual
    print(f"💓 {VIDA}\n")

    # Verificando fim do jogo
    if fim:
        print("🎉🎉🎉PARABÉNS VOCÊ ENCONTROU O ALIENÍGENA🎉🎉🎉")
        break

    # Lendo tentativa do usuário
    while True:
        tentativa = int(input("Em qual árvore está o alienígena: ").strip())
        if tentativa in erros:
            print("Você já tentou está arvore, escolha outra!! \n")
        else:
            break

    # Verificação do jogo
    if tentativa == alien:
        fim = True      # Fim do jogo
    else:
        erros.append(tentativa)       # Listando a tentativa errada
        dano = randint(dano_minimo, dano_maximo)    # Escolhendo dano

        # Mostrando mensagens
        print("\033[31mvocê errou. O alienígena te deu um tiro e você levou...")
        print(f"🔫 {dano} de dano", "\033[m")
        VIDA -= dano
        sleep(3)

# Mostrando jogo após perda
if not fim:
    print()
    print("🤬🤬🤬Você é muito ruim, o alienígena carioca🔫 te matou e fugiu")
    print(f"Ele estava escondido na 🌳{alien}")
    print("FAZ O L")

