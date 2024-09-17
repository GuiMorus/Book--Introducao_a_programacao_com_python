# Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
# O programa deve imprimer 10, 9, 8, ..., 1, 0 e Fogo! na tela.

from time import sleep

# Iniciando repetição para contagem
c = 10  # Contador
while c >= 0:
    # Mostrando contagem
    print(c)
    c = c - 1

    # Delay da contagem
    sleep(1)

# Mostrando mensagem de lançamento
print("O Foguete está decolando!!!")
print("🔥🔥🔥")

