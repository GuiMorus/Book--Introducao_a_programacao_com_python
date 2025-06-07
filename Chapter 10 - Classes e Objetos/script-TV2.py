import controle
import pilha

# ======================
# == DEFININDO CLASSE ==


class Televisão:
    def __init__(self, canal=2, canal_min=1, canal_max=20):
        self.canal = canal
        self.ligada = False
        self.canalMax = canal_max
        self.canalMin = canal_min

    def mudar_canal_sup(self):
        """Método para mudar o canal para cima
        sempre somando +1"""

        # Verificando se o canal chegou ao limite máximo
        if self.canal + 1 <= self.canalMax:
            self.canal += 1                 # Troca de canal
        # Verificando se o canal é o mesmo que o limite
        elif self.canal == self.canalMax:
            self.canal = self.canalMin      # Canal recebe o minimo para formar um loop

    def mudar_canal_inf(self):
        """Método para mudar o canal para baixo
        sempre diminuindo -1"""

        # Verificando se o canal chegou ao limite mínimo
        if self.canal - 1 >= self.canalMin:
            self.canal += 1  # Troca de canal
        # Verificando se o canal é o mesmo que o limite
        elif self.canal == self.canalMin:
            self.canal = self.canalMax  # Canal recebe o máximo para formar um loop


# ===============
# == MAIN CODE ==

# Instanciando um objeto de Televisão()
tv = Televisão()
print(f"Canal atual: {tv.canal}")
print(f"TV está ligada: {tv.ligada}\n")

# Instanciando um objeto de Pilha()
bateria = pilha.Pilha(2)
print(f"Energia atual da bateria: {bateria.energia}\n")

# Instanciando um objeto de ControleRemoto()
control = controle.ControleRemoto(tv, bateria)
control.ligar()
control.canal_mais()
print(f"Canal atual: {tv.canal}")
print(f"TV está ligada: {tv.ligada}")

# Mostrando a bateria após o uso do objeto control
print(f"Energia atual da bateria: {bateria.energia}")
control.canal_menos()
print(f"Canal atual: {tv.canal}")
