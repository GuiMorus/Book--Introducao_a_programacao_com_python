# Criando script de teste para as classes de heranças do Banco TATU
from clientes import Cliente
from contas import Conta, ContaEspecial
from bancos import Banco

# Iniciando objetos
joão = Cliente("João da Silva", "3241-5599")
maria = Cliente("Maria Silva", "7231-9955")
conta1 = Conta([joão], numero="001", saldo=1000)
conta2 = ContaEspecial([maria, joão], numero="002", saldo=500, limite=1000)

# Testes com os objetos
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.extrato()
conta2.saque(1500)
conta1.extrato()
conta2.extrato()
