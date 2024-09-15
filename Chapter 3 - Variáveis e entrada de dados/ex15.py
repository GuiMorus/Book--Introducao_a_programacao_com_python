# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte
# a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias
# de vida um fumante perderá. Exiba o total de dias.

# Iniciando variável
ano_dias = 365

# Introdução
print("-" * 10, "FUMAR NÃO PODE", "-" * 10)

# Resgatando informações
cigarros = int(input("Fumas quanto num dia: ").strip())
anos = int(input("Fumas a quantos anos: ").strip())

# Calculando morte
perdeu = (cigarros * 10) / 1440
vida = perdeu * (ano_dias * anos)

# Mostrando dias perdidos
print(f"Você perdeu: {round(vida)} dias")

# Encerramento
print("-" * 8, "LIVRA-TE DO CIGARRO", "-" * 8)
