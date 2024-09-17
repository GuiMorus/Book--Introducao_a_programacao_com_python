# Modifique o programa anterior de forma que o usuário possa digitar o início e o fim
# da tabuada, em vez de começar com 1 e terminar no 10

# Resgatando início e fim da tabuada
fator = int(input("Começo da multiplicação: "))
fim = int(input("Fim da multiplicação: "))

# Repetição mostrando tabuada
n = 2   # número fator multiplicando

while fator <= fim:
    print(f"{n} x {fator:<3} = {n * fator}")
    fator = fator + 1
