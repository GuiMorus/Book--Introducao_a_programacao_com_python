# Criando script de teste para a classes do Banco TATU
from clientes import Cliente
from contas import Conta
from bancos import Banco

# Iniciando objetos dos clientes
joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

# Iniciando objetos das contas
conta1 = Conta(joão, 1, 1000)
conta2 = Conta([maria, joão], 2, 500)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)
conta1.extrato()
conta2.extrato()
conta1.resumo()

# Fazendo testes com novas contas junto com o objeto do tipo Banco()
print("===== TESTE DOS BANCOS =====")
josé = Cliente("José Vargas", "9721-3000")
contaJM = Conta([joão, maria], 100)
contaJ = Conta([josé], 10)
tatu = Banco("Tatú")
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
contaJM.deposito(1000)
contaJ.deposito(500)
contaJM.saque(40.54)
tatu.listar_contas()
