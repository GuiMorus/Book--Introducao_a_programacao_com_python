# Utilizando a classe Televisão do exercício anterior, crie duas instancias
# especificando o valor de canal_min e canal_max por nome.

# =======================
# == INICIANDO CLASSES ==
# =======================
class Televisão:
    def __init__(self, canal_min=2, canal_max=14):
        self.canal = 2                  # Atributo do canal inicial
        self.canal_max = canal_max      # Atributo do canal máximo
        self.canal_min = canal_min      # Atributo do canal mínimo


# ===============
# == MAIN CODE ==
# ===============

# Instanciando Objeto
tv = Televisão()
print(tv.canal_min)     # Mostrando atributos de cada objeto
print(tv.canal_max)

tv_nova = Televisão(1, 50)
print(tv_nova.canal_min)
print(tv_nova.canal_max)
