# Atualmente, a classe Televisão inicializa o canal com 2. Modifique a classe
# de forma a receber o canal inicial em seu construtor como parâmetro opcional

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

        # Variável para mostrar canal atual
        if mostrar:
            print(f"Canal Atual: {self.canal}")

    # Metodo para mudar de canal para baixo
    def mudar_canal_inf(self, mostrar=False):
        # Verificando troca minima de canal
        if self.canal - 1 >= self.canal_min:
            self.canal -= 1

        # Variável para mostrar canal atual
        if mostrar:
            print(f"Canal Atual: {self.canal}")


# ===== MAIN ===== #
tv = Televisão(100, 1, 7)       # Declarando objeto de Televisão
print(f"Canal atual: {tv.canal}")                       # Mostrando canal atual do objeto
tv.mudar_canal_sup(mostrar=True)                        # Utilizando método de troca de canal
tv.mudar_canal_sup()                                    # Utilizando método de troca de canal
print(f"Canal atual: {tv.canal}")
