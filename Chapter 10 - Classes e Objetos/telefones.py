# Criando classe dos tipos de telefones
from functools import total_ordering

@total_ordering
class TipoTelefone:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"({self.tipo})"

    def __eq__(self, other):
        if other is None:
            return False
        return self.tipo == other.tipo

    def __lt__(self, other):
        return self.tipo < other.tipo


# Criando classe dos telefones
class Telefone:
    def __init__(self, numero, tipo=None):
        self.numero = numero
        self.tipo = tipo

    def __str__(self):
        tipo = self.tipo or ""
        return f"<{tipo}>{self.numero}"

    def __eq__(self, other):
        return self.numero == other.numero and ((self.tipo == other.tipo) or (self.tipo is None or other.tipo is None))

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valor):
        if valor is None or not valor.strip():
            raise ValueError("Número não pode ser None ou em branco")
        self.__numero = valor
