# Declarando classe para representar estados
class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    def inserir_cidade(self, cidade):
        """Este método insere cidades ao objeto do tipo Estado()
        Espera-se um objeto do tipo Cidade()"""
        self.cidades.append(cidade)

    def mostrar_habitantes(self, msg=True):
        """Este método mostra o total de habitantes que há em
        um objeto do tipo Estado(). Soma-se os habitantes de cada
        objeto do tipo Cidade()"""
        habitantes = 0
        for i in self.cidades:
            habitantes += i.habitantes

        # Verificando parametro msg para mostrar texto no console
        if msg:
            print(f"Total de habitantes do estado {self.nome}: {habitantes:,}".replace(",", "."))
        return habitantes
