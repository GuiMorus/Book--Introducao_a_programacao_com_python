# Fazendo uma Classe de uma TV
class Televisão:
    def __init__(self, canal_min, canal_max):
        self.ligada = False
        self.canal = 2
        self.canal_min = canal_min
        self.canal_max = canal_max

    def mudar_canal_sup(self):
        """Muda para os canais superiores
        sempre para um canal acima: atual + 1
        Para no valor definido em canal_max"""
        if self.canal + 1 <= self.canal_max:
            self.canal += 1

    def mudar_canal_inf(self):
        """Muda para os canais inferiores
            sempre para um canal abaixo: atual - 1
            Para no valor definido em canal_min"""
        if self.canal - 1 >= self.canal_min:
            self.canal -= 1


# Instanciando objetos
tv_quarto = Televisão(1, 99)     # tv_quarto é um Objeto da Classe Televisão()
print(tv_quarto.ligada)                             # Mostrando atributo "ligada" do Objeto
print(tv_quarto.canal)                              # Mostrando atributo "canal" do Objeto

tv_sala = Televisão(1, 50)       # tv_sala é um Objeto da Classe Televisão()
tv_sala.ligada = True                               # Definindo atributo "ligada" do Objeto
tv_sala.canal = 4                                   # Definindo atributo "canal" do Objeto
print(tv_sala.ligada)                               # Mostrando atributo "ligada" do Objeto
print(tv_sala.canal)                                # Mostrando atributo "canal" do Objeto

for x in range(0, 120):
    tv_sala.mudar_canal_sup()
print(tv_sala.canal)

for i in range(0, 120):
    tv_sala.mudar_canal_inf()
print(tv_sala.canal)
