# Adicione os atributos tamanho e marca à classe Televisão.
# Crie dois objetos Televisão e atribua tamanhos e marcas diferentes.
# Depois, imprima o valor desses atributos de forma a confimar a independência
# dos valores de cada instância(objeto)

# Criando Classe Televisão
class Televisão:
    def __init__(self):
        self.ligado = False
        self.canal = 2
        self.marca = ""
        self.tamanho = 15


# Instânciando Objetos e os seus atributos
tv_sala = Televisão()
tv_sala.ligado = True
tv_sala.canal = 1
tv_sala.marca = "Samsung"
tv_sala.tamanho = 12

tv_quarto = Televisão()
tv_quarto.ligado = False
tv_quarto.canal = 2
tv_quarto.marca = "LG"
tv_quarto.tamanho = 20

# Mostrando atributos dos Objetos
print("[TV DA SALA]")
print(f"Marca: {tv_sala.marca}")
print(f"Tamanho: {tv_sala.tamanho} polegadas")

print("\n[TV DO QUARTO]")
print(f"Marca: {tv_quarto.marca}")
print(f"Tamanho: {tv_quarto.tamanho} polegadas")
