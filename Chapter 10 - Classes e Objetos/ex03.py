# Modifique a classe Televisão de forma que, se pedirmos para mudar o canal para
# baixo, além do mínimo, ele vá para o canal máximo. Se mudarmos para cima,
# além do canal máximo, que volte ao canal mínimo

# Declarando Classe
class Televisão:
    def __init__(self, canal_max, canal_min, canal=2):
        self.ligado = False
        self.canal = canal
        self.canal_max = canal_max
        self.canal_min = canal_min

    # Metodo para mudar de canal para cima
    def mudar_canal_sup(self, mostrar=False):
        # Verificando troca maxima de canal
        if self.canal + 1 <= self.canal_max:
            self.canal += 1     # Trocando canal para cima
        # Verificando se o canal é igual ao máximo
        elif self.canal == self.canal_max:
            self.canal = self.canal_min     # Trocando canal para o minimo, formando um loop

        # Variável para mostrar canal atual
        if mostrar:
            print(f"Canal Atual: {self.canal}")

    # Metodo para mudar de canal para baixo
    def mudar_canal_inf(self, mostrar=False):
        # Verificando troca minima de canal
        if self.canal - 1 >= self.canal_min:
            self.canal -= 1
        # Verificando se o canal é igual ao máximo
        elif self.canal == self.canal_min:
            self.canal = self.canal_max     # Trocando canal para o minimo, formando um loop

        # Variável para mostrar canal atual
        if mostrar:
            print(f"Canal Atual: {self.canal}")


# ===== MAIN ===== #
tv = Televisão(100, 1, 99)     # Declarando objeto de Televisão
print(f"Canal atual: {tv.canal}")                       # Mostrando canal atual do objeto
tv.mudar_canal_sup(mostrar=True)                        # Utilizando método de troca de canal
tv.mudar_canal_sup(True)                                # Utilizando método de troca de canal
tv.mudar_canal_inf(True)
print(f"Canal atual: {tv.canal}")
