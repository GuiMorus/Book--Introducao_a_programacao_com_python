# Programa 8.19: Módulo entrada
def valida_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            v = int(input(mensagem))
            if maximo >= v >= minimo:
                return v
            else:
                print(f"Digite um valor entre {minimo} e {maximo}")
        except ValueError:
            print("Você deve digitar um número inteiro")
