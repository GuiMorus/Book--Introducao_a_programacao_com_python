# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação:
# R para residênciais;
# I para industriais;
# C para comércios;
# Calcule o preço a pagar de acordo com a tabela descrita no livro.

# Iniciando variáveis
pagar = 0
taxa = 0

# Introdução
print("-" * 10, "RIC ELETRICIDADES", "-" * 10)

# Recolhendo informações do usuário
consumo = float(input("kWh consumida: ").strip().replace(',', '.'))
print("[ R ] - Residêncial")
print("[ I ] - Indústrial")
print("[ C ] - Comercial")
tipo = input("SELECIONE O TIPO: ").lower()

# Verificando e cobrando pelo tipo
if tipo == 'r' or ("resid" in tipo):
    taxa = 0.40 if consumo <= 500 else 0.65

elif tipo == 'i' or ("ind" in tipo):
    taxa = 0.55 if consumo <= 5000 else 0.60

elif tipo == 'c' or ("comer" in tipo):
    taxa = 0.55 if consumo <= 1000 else 0.60

else:
    print("Tipo inválido")

# Mostrando total a pagar
print(f"Total a pagar: R${consumo * taxa:.2f}")
