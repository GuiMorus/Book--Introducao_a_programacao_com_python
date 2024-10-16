# Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres
# da segunda foram retirados da primeira.
#
# 1° string: AATTGGAA
# 2° string: TG
# resultado -> string: AAAA

# Iniciando variáveis
txt1 = "AATTGGAA"
txt2 = "TG"

# Gerando terceira string com diferença
conjunto = set(txt1) - set(txt2)
txt3 = "".join(conjunto)

# Mostrando resultado
print(f"1° String: {txt1}")
print(f"2° String: {txt2}")
print(f"3° String por diferença: {txt3 * txt1.count('A')}")
