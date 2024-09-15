# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
# pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$ 0,15 por km rodado.

# **Introdução**
print("-" * 20, "CARBnB", "-" * 20)

# Iniciando variáveis
km = float(input("Digite a quantidade de Km percorridos: ").strip().replace(',', '.'))
dias = int(input("Digite quantos dias foi alugado o carro: ").strip())

# Calculando o valor do aluguel do carro
pagar = 60 * dias + km * 0.15
_pagar = str(f"{pagar:.2f}").replace('.', ',')

# Mostrando mensagem de pagamento
print("\n=== RESUMO", "=" * 15)
print(f"Dias Alugados: {dias} dias")
print(f"Km Percorridos: {km:.2f} KM")
print(f"Total: R${_pagar}")

# **Encerramento**
print("-" * 21, "FIM", "-" * 22)
