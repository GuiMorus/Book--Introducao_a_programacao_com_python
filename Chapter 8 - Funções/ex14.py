# Altere o Programa 8.22 de forma que o usuário tenha três chances de acertar o número.
# O programa termina se o usuário acertar ou errar as três vezes.

from random import randint

# Iniciando variáveis
aleatorio = randint(1, 10)

# Repetição dando oportunidades do usuário acertar
for c in range(3):
    # Lendo número escolhido pelo usuário
    usuario = int(input("Escolha um número entre 1 e 10: ").strip())

    # Verificando resultados
    if usuario == aleatorio:
        print("Parabens meu bom!! você advinhou o número aleatório, jogue na mega")
        break
    else:
        print("Não foi dessa vez")
