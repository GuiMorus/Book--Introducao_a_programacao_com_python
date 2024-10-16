# Escreva um programa que leia três strings. Imprima o resultado da substituição
# na primeira, dos caracteres da segunda pelos da terceira.
#
# 1° string: AATTCGAA
# 2° string: TG
# 3° string: AAAACCAA

# Iniciando variáveis
txt1 = "AATTCGAA"
txt2 = "TG"
txt3 = "AC"

# Gerando 4° string por replace
txt4 = txt1

for i in txt1:
    # Verificando letra
    if i == txt2[0]:
        txt4 = txt4.replace(i, txt3[0])

    if i == txt2[1]:
        txt4 = txt4.replace(i, txt3[1])

# Mostrando resultado
print(f"1° String: {txt1}")
print(f"String de comparação: {txt2}")
print(f"String de substituição: {txt3}")
print(f"Resultado: {txt4}")
