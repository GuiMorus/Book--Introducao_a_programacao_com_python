# Fazendo classe de lista única utilizando collections
from collections import UserList


class ListaUnica(UserList):
    def __init__(self, elem_classe, enumerable=None):
        super().__init__(enumerable)
        self.elem_classe = elem_classe

    def append(self, elem):
        self.verificar_tipo(elem)
        if elem not in self.data:
            super().append(elem)

    def __setitem__(self, posição, elem):
        self.verificar_tipo(elem)
        if elem not in self.data:
            super().__setitem__(posição, elem)

    def verificar_tipo(self, elem):
        if not isinstance(elem, self.elem_classe):
            raise TypeError("Tipo Inválido")

    def extend(self, other):
        self.verificar_tipo(other)
        if other not in self.data:
            super().extend(other)
