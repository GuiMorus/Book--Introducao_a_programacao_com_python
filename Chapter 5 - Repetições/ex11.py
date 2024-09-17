# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

# Introdução
print("-" * 10, "QUANTO VOCÊ POUPARÁ?", "-" * 10)

# Recolhendo informações iniciais
deposito = float(input("Qual o depósito inicial: R$").strip().replace(',', '.'))
taxa = float(input("Qual a taxa de juros ao mês: ").strip().replace(',', '.').replace('%', ''))

# Calculando e mostrando montante
c = 1  # contador
montante = deposito

while c <= 24:
    montante = montante + (montante * taxa / 100)
    print(f"{c}° mês = R${montante:.2f}")
    c += 1
