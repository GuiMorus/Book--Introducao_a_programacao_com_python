# Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira
# e imprima a posição de início.
#
# 1° string: AABBEFAATT
# 2° string: BE
# Resultado: BE encontrado na posição 3 de AABBEFAATT

# Iniciando variáveis
primeira = "AABBEFAATT"
segunda = "BE"

# Verificando string
print(f"1° String: {primeira}")
print(f"2° string: {segunda}")
print(f"posição encontrada: {primeira.find(segunda)}")
