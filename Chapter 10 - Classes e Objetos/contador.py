# Criando classe contador
class Contador:
    # Iniciando atributos
    instancias = 0

    # Criando metodo construtor
    def __init__(self):
        self.contador = 0
        Contador.instancias += 1

    # Definindo incrementador
    def incrementa(self):
        self.contador += 1
