# Escreva um programa qpara exibir todas as palavras de uma frase. Considere
# que uma palavra termina com um espaço em branco ou quando a string terminar.

# Introdução
print("-" * 10, "QUANTAS PALAVRAS TÊM?", "-" * 10)
frase = input("Digite uma frase: ").strip()

# Gerando contagem das palavras
palavras = frase.split()

# Mostrando resultado
print(f"Foi identificado {len(palavras)} palavra(s).")
