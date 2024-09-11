# Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância
# a percorrer e a velocidade média esperada para a viagem.

# Mensagem Inicial
print("=" * 13, "TEMPO DE VIAGEM", "=" * 13)    # Introdução
print("OBS: Digite apenas números")

# Recuperando informações do usuário
distancia = input("Qual a distância da viagem em Km: ")
velocidade = input("Qual a velocidade média em Km/h: ")

# Tratando dados
distancia = float(distancia.replace(',', '.').strip())
velocidade = float(velocidade.replace(',', '.').strip())

# Mostrando resultado
tempo = distancia / velocidade
print(f"O tempo de viagem é de {tempo:.2f} horas")
print("=" * 43)     # Encerramento
