# Escreva um programa que peça ao usuário que digite uma frase e imprima quantas
# vogais ela contém. Não considere maiúsculas e minúsculas como diferentes.
# Exemplo: uma frase como "A casa" deve imprimir: 3 "a(s)"

# Lendo frase digitada pelo usuário
frase = input("Digite uma frase: ").strip()

# Mostrando resultado
print(f"A frase: {frase}. têm:")
frase = frase.lower()
print(f"a: {frase.count('a')}")
print(f"e: {frase.count('e')}")
print(f"i: {frase.count('i')}")
print(f"o: {frase.count('o')}")
print(f"u: {frase.count('u')}")
