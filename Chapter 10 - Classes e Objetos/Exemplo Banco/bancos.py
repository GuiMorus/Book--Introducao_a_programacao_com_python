# Declarando classe Banco() para guardar as contas ativas
class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def abre_conta(self, conta):
        """Este método serve para adicionar uma nova conta
        ao objeto do banco"""
        self.contas.append(conta)

    def listar_contas(self):
        """Este método mostra os resumos de cada objeto do
        tipo Conta() contidos dentro das contas salvas nele"""
        for c in self.contas:
            c.resumo()
