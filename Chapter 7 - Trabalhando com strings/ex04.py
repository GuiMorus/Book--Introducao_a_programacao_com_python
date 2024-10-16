# Escreva um programa que leia uma string e imprima quantas vezes cada caractere
# aparece nesta string
#
# String: TTAAC
# Resultado -> T: 2x; A: 2x; C: 1x

# Iniciando variáveis
texto = "TTAAC"

# Mostrando resultado
print(f"Texto: {texto}")
print(f"T: {texto.count('T')}x")
print(f"A: {texto.count('A')}x")
print(f"C: {texto.count('C')}x")
