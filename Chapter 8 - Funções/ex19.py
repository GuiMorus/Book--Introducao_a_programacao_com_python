# Escreva um generator capaz de gerar a sequência dos números primos
def verificar_primo(x):
    primo = True    # Iniciando variável lógica
    # Verificando se o número é maior que 1
    if x <= 1:
        primo = False

    # Verificando se o numémo é divisível por 2(e diferente de 2)
    if x != 2 and x % 2 == 0:
        primo = False

    # Verificando a divisão pela raiz do número
    raiz = int(x ** 0.5)
    for valor in range(2, raiz + 1):
        if x % valor == 0:
            primo = False

    # Retornando resultado
    return primo


# Gerador de números primos
def primos(limite):
    primo = 2   # Começando pelo primeiro primo
    while primo <= limite:
        # Verificando primo
        if verificar_primo(primo):
            yield primo     # Retornando iterável

        primo += 1      # Incrementando variável


print("Forma com função")
print(list(primos(100)))

# Lista de primops com List Comprehension
print("Forma com List Comprehension")
numeros_primos = [x for x in range(2, 101) if verificar_primo(x)]
print(numeros_primos)
