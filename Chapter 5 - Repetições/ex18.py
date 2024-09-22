# Modifique o programa (5.1) para também trabalhar com notas de R$ 100

# Programa 5.1: Contagem de cédulas
valor = int(input("Digite o valor a pagar: R$").strip().replace(',', '.'))
cedulas = 0
atual = 100
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} cédula(s) de R${atual}")
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1

        cedulas = 0
