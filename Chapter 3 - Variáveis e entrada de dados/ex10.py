# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do
# salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário

# Recuperando valores do usuário
print("=" * 13, "CALCULO SALARIAL", "=" * 13)   # Introdução

salario = input("Digite seu salário: R$")
porcentagem = input("Digite a porcentagem de aumento: ")

# Tratando os dados
salario = float(salario.replace(',', '.').strip())
porcentagem = float(porcentagem.replace('%', '').replace(',', '.').strip())

# Mostrando o valor do acréscimo do salário
resultado = salario * (1 + porcentagem / 100)
print(f"Novo salário com {porcentagem:.0f}% de aumento: R${resultado:.2f}")
print("=" * 44)     # Encerramento
