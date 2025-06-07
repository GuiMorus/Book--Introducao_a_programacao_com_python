# Extendendo classes
class ControleRemoto:
    def __init__(self, tv, pilha):
        """Esta classe espera um objeto do tipo Televisão()
        para funcionar corretamente os seus paramentros

        Também espera-se um objeto do tipo Pilha() com
        base em valores de consumo para poder
        executar os métodos do objeto anterior"""
        self.tv = tv
        self.pilha = pilha

    def ligar(self):
        """Ao chamar este método, ele modifica o atributo
        do objeto que foi passado, no caso o atributo ligada"""
        # Verificando se há energia na pilha
        if self.pilha.consumir(1):
            self.tv.ligada = True   # Caso haja bateria, o método é executado

    def desligar(self):
        """Ao chamar este método, ele modifica o atributo
        do objeto que foi passado, no caso o atributo ligada"""
        # Verificando se há energia na pilha
        if self.pilha.consumir(1):
            self.tv.ligada = False  # Caso haja bateria, o método é executado

    def canal_mais(self):
        """Ao chamar este método, ele chama um método
        dentro do objeto que foi passado"""
        # Verificando se há energia na pilha
        if self.pilha.consumir(1):
            self.tv.mudar_canal_sup()

    def canal_menos(self):
        """Ao chamar este método, ele chama um método
        dentro do objeto que foi passado"""
        # Verificando se há energia na pilha
        if self.pilha.consumir(1):
            self.tv.mudar_canal_inf()
