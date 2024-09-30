# Programa 6.20: Ordenação pelo método de bolhas "Bubble Sort"
lista = [7, 4, 3, 12, 8]
fim = len(lista)    # quantidade de elementos da lista

# Verificando se há no mínimo 2 elementos
while fim > 1:
    trocou = False  # Troca não realizada
    x = 0   # indice

    while x < (fim - 1):
        # Comparação em si
        if lista[x] > lista[x + 1]:
            trocou = True               # Troca realizada
            temp = lista[x]             # Guardando valor do primeiro índice
            lista[x] = lista[x + 1]     # Primeiro elemento recebe o segundo elemento( que é menor )
            lista[x + 1] = temp         # Segundo elemento recebe o primeiro elemento( guardado em temp )
        x += 1  # incrementando indice

    # Verificando se algo foi trocado na repetição anterior
    if not trocou:
        break

    fim -= 1

# Mostrando resultado
for e in lista:
    print(e)
