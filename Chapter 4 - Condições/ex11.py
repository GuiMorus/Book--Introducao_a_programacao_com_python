# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos
# a pagar. O valor da prestação mensal não pode ser superior a 30% do salário.
#
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo
# número de meses a pagar.

# Introdução
print("-" * 12, "SEU SONHO, SUA CASA", "-" * 12)
print("Vamos aprovar-lhe o empréstimo de sua casa\n")

# Recolhendo informações necessárias
casa = float(input("Qual o valor da casa: R$").strip().replace(',', '.'))
salario = float(input("Qual o seu salário(bruto): R$").strip().replace(',', '.'))
anos = int(input("Deseja pagar em quantos anos: ").strip())

# Verificando possibilidade de empréstimo
mensal = anos * 12
limite_salarial = salario - (salario * 0.30)
parcelamento = casa / mensal

if limite_salarial < parcelamento:
    print("\033[31m" + "EMPRÉSTIMO NEGADO" + "\033[m")
    print("-" * 9, "seu sonho terá de esperar", "-" * 9)
else:
    print("\033[32m" + "EMPRÉSTIMO APROVADO" + "\033[m")
    print("-" * 10, "seu sonho realizar-se-á", "-" * 10)
