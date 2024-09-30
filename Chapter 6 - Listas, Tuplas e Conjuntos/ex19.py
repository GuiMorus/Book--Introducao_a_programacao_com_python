# Altere o Programa 6.22 de forma a solicitar ao usuário o produto e a quantidade vendida.
# Verifique se o nome do produto digitado existe no dicionário, e só então efetue a baixa em estoque.

# Programa 6.22: Exemplo de dicionário com estoque
# e operações de venda (modificado e comentado)

# Iniciando variáveis
estoque = {
            "tomate": [1000, 2.30],
            "alface": [500, 0.45],
            "batata": [2001, 1.20],
            "feijão": [100, 1.50]
            }
total = 0   # Valor a pagar

# Recolhendo produtos e quantidades
item = input("Qual produto deseja: ").strip().lower()
multiplicador = int(input("Qual a quantidade: ").strip())

# Verificando existência do produto
if item in estoque.keys():
    venda = [item, multiplicador]
    produto, quantidade = venda
else:
    print("PRODUTO NÃO ENCONTRADO")
    exit()

# Verificando possibilidade de venda
if quantidade <= estoque[produto][0]:

    # Recolhendo preço e definindo custo
    preço = estoque[produto][1]
    custo = preço * quantidade
    total += custo

    # Ajustando estoque do produto
    estoque[produto][0] -= quantidade

else:
    print("Falta de estoque")

# Mostrando resultado
print(f"{'Produto':<20} {'Quantidade':<20} {'Preço':<12} {'Custo'}")
print(f"{produto:<20} {quantidade:<20} R${preço:<10.2f} R${custo:.2f}")
print(f"Total a pagar: R${total:.2f}")

# Mostrando estoque
print("\nESTOQUE")
for chave, dados in estoque.items():
    print(f"Produto: {chave}")
    print(f"Quantidade: {dados[0]}")
    print(f"Preço: R${dados[1]:.2f}")
    print("-")
