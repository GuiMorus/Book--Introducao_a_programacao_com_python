# Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto.
# Considere que pagam imposto pessoas cujo salário é maior que R$1.200,00

# Iniciando variável
margem = 1200

# Recuperando salário do usuário
salario = float(input("Digite o seu salário: R$").strip().replace(',', '.'))

# Mostrando mensagem
pagar = salario > margem
print(f"Salário: R${salario:.2f}")
print(f"Pagar imposto: {pagar}")
