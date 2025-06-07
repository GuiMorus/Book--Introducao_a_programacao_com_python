class Pilha:
    def __init__(self, energia=100):
        """Esta classe espera um valor de energia para iniciar
        o seu objeto.

        DEFALUT VALUES:
        energia = 100"""
        self.energia = energia

    def consumir(self, consumo):
        """Este método espera um valor de consumo para
        retirar da energia do objeto do tipo Pilha()"""
        # Verificando se ainda há energia
        if consumo > self.energia:
            consumo = self.energia      # Entrega a energia que tem atualmente
        self.energia -= consumo     # A energia(bateria) da pilha é consumida com base no consumo
        return consumo
