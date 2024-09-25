# Modifique o exemplo para pesquisar 2 valores. Em vez de apenas p, leia outro valor v
# que também será procurado. Na impressão, indique qual dos valores foi achado primeiro

# Programa 6.9: Pesquisa sequencial
L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite o outro valor a procurar: "))
achou = False
x = 0
primeiro = 0

while x < len(L):
    if L[x] == p:
        primeiro = L[x] if primeiro == 0 else primeiro
        print(f"{p} achado na posição {x}")

    if L[x] == v:
        primeiro = L[x] if primeiro == 0 else primeiro
        print(f"{v} achado na posição {x}")

    x += 1

print(f"O primeiro valor achado foi {primeiro}")

