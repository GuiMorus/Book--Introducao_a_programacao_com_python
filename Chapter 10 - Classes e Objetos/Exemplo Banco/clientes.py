# Gerando Classe dos clientes do Banco Tatu
class Cliente:
    def __init__(self, nome, telefone):
        self.nome = str(nome).title().strip()
        self.telefone = telefone
