# Criando classe com nomes
from functools import total_ordering


@total_ordering
class Nome:
    # Iniciando Construtor
    def __init__(self, nome):
        self.nome = nome

    # Definindo str
    def __str__(self):
        return self.nome

    # Definindo representação
    def __repr__(self):
        return f"<Classe {type(self).__name__} em 0x{id(self):x} Nome: {self.__nome} Chave: {self.__chave}>"

    # Definindo igualdade
    def __eq__(self, other):
        print("__eq__ Chamado")
        return self.nome == other.nome

    # Definindo maior que e menor que
    def __lt__(self, other):
        print("__lt__ Chamado")
        return self.nome < other.nome

    @property   # Definindo o "get" da classe
    def nome(self):
        return self.__nome

    @nome.setter    # Definindo o "set" da classe
    def nome(self, valor):
        if valor is None or not valor.strip():
            raise ValueError("Nome não pode ser nule nem em branco")
        self.__nome = valor
        self.__chave = Nome.CriarChave(valor)

    @staticmethod   # Criando método estático para a chave
    def CriarChave(nome):
        return nome.strip().lower()
