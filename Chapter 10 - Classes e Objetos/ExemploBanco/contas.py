# Gerando classe para as contas bancárias dos clientes
class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        # Mostrando informações da conta
        print(f"CC Número: {self.numero}\nSaldo: {self.saldo:10.2f}")

        # Verificando se há mais de um cliente      | ex09
        if isinstance(self.clientes, list):
            # Mostrando informação de cada cliente
            for cliente in self.clientes:
                print(f"Cliente: {cliente.nome} | Telefone: {cliente.telefone}\n")
        else:
            print(f"Cliente: {self.clientes.nome} | Telefone: {self.clientes.telefone}\n")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True     # ex12
        else:
            print("SALDO INSULFICIENTE")        # Ex08
            return False

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print("===== EXTRATO DA CONTA =====")
        for operação in self.operações:
            print(f"{operação[0]:10s} R${operação[1]:10.2f}")
        print(f"\n    Saldo: R${self.saldo:10.2f}")


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True     # ex12
        return False

    def extrato(self):
        print("===== EXTRATO DA CONTA =====")
        for operação in self.operações:
            print(f"{operação[0]:10s} R${operação[1]:10.2f}")
        print(f"\n    Saldo: R${self.saldo:10.2f}")
        # ex13 Altere a classe de forma que o extrato exiba o limite e total disponivel para saque
        print(f"    Limite Especial: {self.limite}")
        print(f"    Disponível para saque {(self.limite + self.saldo)}")
