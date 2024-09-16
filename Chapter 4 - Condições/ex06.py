# Escreva um programa que pergunte a distância que um passageiro deseja percorer em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km,
# e R$ 0,45 para viagens mais longas

# Introdução
print("-" * 12, "CALCULADORA DE PASSAGEM", "-" * 12)

# Recolhendo distância da viagem
distancia = float(input("Qual a distância da viagem(em Km): ").strip().replace(',', '.'))

# Iniciando variável
taxa = 0.50 if distancia <= 200 else 0.45

# Mostrando mensagem
print(f"Com uma viagem de {distancia} Km")
print(f"Pagará R${(distancia * taxa):.2f}")
