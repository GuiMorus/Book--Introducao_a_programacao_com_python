# Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar
# ao usuário que digite o código do produto e a quantidade comprada.
#
# Utilize a tabela de códigos a seguir para obter o preço de cada produto.
#
# Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer
# outro código deve gerar a mensagem de erro "Código inválido".

# Iniciando variáveis
total = 0               # total da compra
encontrado = False      # variável para item não encontrado
produtos = [
            [1, 'Bala colorida', 0.50], [2, 'Chocolate', 1],
            [3, 'Bolacha', 4], [5, 'Meias', 7], [9, 'Luvas', 8]
        ]

# Introdução
print("-" * 10, "pequena máquina registradora", "-" * 10)
print("Digite o código do produto para comprá-lo")
print("_" * 40)
print(f"{'CÓDIGO':<10} {'PRODUTO':<20} {'PREÇO'}")

# Repetição montando tabela
for c in range(0, 5):
    print(f"{produtos[c][0]:<10} {produtos[c][1]:<20} R${produtos[c][2]:.2f}")

print("_" * 40)

# Loop do programa principal
while True:

    # Recolhendo produto e quantidade
    escolha = int(input("\nDigite o código do produto: ").strip())

    # Parando programa caso escolha seja 0
    if escolha == 0:
        break

    quantidade = int(input("Quantidade: ").strip())

    # Somando produto x quantidade
    for c in produtos:
        # Verificando existência da escolha
        if c[0] == escolha:
            total += c[2] * quantidade
            encontrado = True   # item encontrado

    # Mensagem de erro caso item não encontrado
    if not encontrado:
        print("\033[31m" + "PRODUTO NÃO ENCONTRADO", "\033[m")

    # Reiniciando variável encontrado
    encontrado = False

# Mostrando total da compra
print(f"Total da compra R${total:.2f}")
