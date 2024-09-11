# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
# Calcule o total em segundos.

# Recuperando valores do tempo
print("=" * 12, "CONVERSOR DE SEGUNDOS", "=" * 12)      # Introdução
print("Digite os valores para a conversão em segundos")

dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

# Convertendo e mostrando o resultado em segundos
dias_seg = dias * 86400
horas_seg = horas * 3600
minutos_seg = minutos * 60
resultado = dias_seg + horas_seg + minutos_seg + segundos

print(f"Total em segundos: {resultado}")
print("=" * 46)     # Encerramento
