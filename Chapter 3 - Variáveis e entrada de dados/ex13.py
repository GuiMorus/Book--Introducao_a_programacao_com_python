# Escreva um programa que converta uma temperatura digitada em °C em °F.

# Resgatando temperatura em celcius
print("=" * 5, "CONVERSOR DE TEMPERATURA", "=" * 5)    # Introdução
celcius = float(input("Digite a temperatura °C: ").replace(',', '.').strip())

# Mostrando resultado
fah = (9 * celcius / 5) + 32
print(f"{celcius}ºC equivale {fah}°F")
print("=" * 36)     # Encerramento
