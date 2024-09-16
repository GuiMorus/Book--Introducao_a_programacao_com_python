# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse
# 80 Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor
# da multa, cobrando R$ 5,00 por km acima de 80 km/h

# Iniciando variáveis
limite = 80
multa = 0

# Introdução
print("-" * 15, "RADAR ONLINE", "-" * 15)

# Recolhendo velocidade do usuário
velocidade = float(input("Quantos Km/h está o carro no momento: ").strip().replace(',', '.'))

# Verificando multa a ser aplicada
if velocidade > limite:
    print("VOCÊ FOI MULTADO")
    multa = (velocidade - limite) * 5   # Aplicando formula da multa

else:
    print("Tudo certo nesta viagem")

# Mostrando informações
print(f'{"Velocidade Atual:":<23} {"Limite:":<12} Multa:')
print(f"{str(velocidade) + ' Km/h':<23} {str(limite) + ' Km/h':<12} R${multa:.2f}")
