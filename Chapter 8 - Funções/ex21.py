# Escreva uma funçãp que gere os números como a função range()
# Essa função recebe três parâmetros e o seu comportamento muda se passarmos um, dois ou
# até três parametros. Chame-a de faixa

def faixa(inicio=0, fim=0, passo=1):
    # Verificando se o início é maior que o fim
    if inicio > fim:
        # Caso o passo seja positivo começa a contar pelo fim
        if passo > 0:
            while fim <= inicio:
                yield fim
                fim += passo

        # Caso o passo seja positivo começa a contar pelo início
        else:
            while inicio >= fim:
                yield inicio
                inicio += passo

    # Verificando se o fim é maior que o início
    else:
        # Caso o passo seja positivo, começa contando pelo início
        if passo > 0:
            while inicio <= fim:
                yield inicio
                inicio += passo
        # Caso o passo seja negativo, começa contando pelo fim
        else:
            while fim >= inicio:
                yield fim
                fim += passo


# Mostrando o resultado da faixa. Tente mudar os valores e intervalos
print(list(faixa(11, 10, 2)))
