# Escreva um programa que pergunte o valor inicial de uma dívida e o juros mensal.
# Pergunte também o valor mensal que será pago. Mostre o número de meses para que a dívida
# seja paga, o total pago e o total de juros pago.

# Introdução
print("-" * 10, "Pague suas Dívidas", "-" * 10)

# Recolhendo informações iniciais
divida = float(input("Qual o valor inicial da sua dívida: R$").strip().replace(',', '.'))
taxa = float(input("Qual o juros mensal: ").strip().replace(',', '.').replace('%', ''))
mensal = float(input("Quanto pagará por mês: R$").strip().replace(',', '.'))

# Repetição fazendo os calculos
c = 1   # contador
restante = divida
pago = mensal

while restante > 0:
    restante = restante + (restante * taxa / 100)
    print(f"{c}° mês a dívida será de: R${restante:.2f}")
    restante -= mensal

    pago += mensal
    c += 1

# Mostrando juros pago
pago = pago - (restante + mensal)
juros = pago - divida
print(f"\nVocê pagou R${pago:.2f}")
print(f"Houve um juros de R${juros:.2f} comparado à dívida inicial de R${divida:.2f}")
