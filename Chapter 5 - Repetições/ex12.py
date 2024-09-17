# Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
# Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo
# de juros do mês seguinte.

# Introdução
print("-" * 10, "QUANTO VOCÊ POUPARÁ? 2.0", "-" * 10)

# Recolhendo informações iniciais
deposito = float(input("Qual o depósito inicial: R$").strip().replace(',', '.'))
mensal = float(input("Quanto vai depositar por mês: R$").strip().replace(',', '.'))
taxa = float(input("Qual a taxa por mês: ").strip().replace(',', '.').replace('%', ''))
anos = int(input("Quantos anos quer o calculo: ").strip())

# Calculando montante
c = 1
montante = deposito

while c <= (anos * 12):
    montante = montante + mensal + (montante * taxa / 100)
    print(f"{c}° mês = R${montante:.2f}")
    c += 1
