# Utilizando o que aprendemos com funções, modifique o construtor
# da classe Televisão de forma que canal_min e canal_max sejam parâmetros
# opcionais, em que canal_min vale 2 e calan_max vale 14.

# =======================
# == INICIANDO CLASSES ==
# =======================
class Televisão:
    def __init__(self, canal_min=2, canal_max=14):
        self.canal = 2                  # Atributo do canal inicial
        self.canal_max = canal_max      # Atributo do canal máximo
        self.canal_min = canal_min      # Atributo do canal mínimo
