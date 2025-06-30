# Criando classe de lista única
class ListaUnica:
    def __init__(self, elem_classe):
        self.lista = []
        self.elem_classe = elem_classe

    def __len__(self):
        return len(self.lista)

    def __iter__(self):
        return iter(self.lista)

    def __getitem__(self, posição):
        return self.lista[posição]

    def indiceValido(self, indice):
        return 0 <= indice < len(self.lista)

    def adicionar(self, elem):
        if self.pesquisar(elem) == -1:
            self.lista.append(elem)

    def remover(self, elem):
        self.lista.remover(elem)

    def pesquisar(self, elem):
        self.verificar_tipo(elem)
        try:
            return self.lista.index(elem)
        except ValueError:
            return -1

    def verificar_tipo(self, elem):
        if not isinstance(elem, self.elem_classe):
            raise TypeError("Tipo Inválido")

    def ordenar(self, chave=None):
        self.lista.sort(key=chave)

