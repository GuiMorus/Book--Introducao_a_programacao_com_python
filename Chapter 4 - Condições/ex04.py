# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1.250,00 calcule um aumento de 10%. Para inferiores ou
# iguais, de 15%.

# Introdução
print("-" * 10, "QUANTO MENOS, MAIS", "-" * 10)

# Lendo o salário
salario = float(input("Digite seu salário: R$").strip().replace(',', '.'))

# Verificando e calculando aumento
if salario > 1250:
    aumento = salario * 1.10
    porcent = 10
else:
    aumento = salario * 1.15
    porcent = 15

# Mensagem final
print(f"Você obteve {porcent}% de aumento")
print(f"Novo salário: R${aumento:.2f}")
