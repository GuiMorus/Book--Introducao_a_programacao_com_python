# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.

# Resgatando valores digitados pelo usuário
print("=" * 10, "PROGRAMA DE DESCONTO", "=" * 10)   # Introdução
produto = input("Qual o preço da mercadoria: R$")
desconto = input("Qual o percentual de desconto: ")

# Tratando os dados
produto = float(produto.replace(',', '.').strip())
desconto = float(desconto.replace(',', '.').replace('%', '').strip())

# Mostrando resultado
valor = produto - (produto * (desconto / 100))
print(f"Novo valor a pagar: R${valor:.2f}")
print("=" * 42)     # Encerramento
