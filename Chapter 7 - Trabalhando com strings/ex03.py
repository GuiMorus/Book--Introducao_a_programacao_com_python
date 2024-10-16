# Escreva um programa que leia duas strings e gere uma terceira apenas com os
# caracteres que aparecem em uma delas.
#
# 1° string: CTA
# 2° string: ABC
# resultado -> 3° string: BT
# Obs: a ordem dos caracteres da terceira string não é importante

# Iniciando variáveis
txt1 = "CTA"
txt2 = "ABC"

# Gerando terceira string com intersecção
conjunto = set(txt1) ^ set(txt2)
txt3 = "".join(conjunto)

# Mostrando resultado
print(f"1° String: {txt1}")
print(f"2° String: {txt2}")
print(f"3° String gerada por intersecção: {txt3}")
