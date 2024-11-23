# Escreva uma função que receba uma string e uma lista. A função deve comparar a string
# passada com os elementos da lista, também, passada como parâmetro.
# Retorne verdadeiro se a string for encontrada dentro da lista, e falso, caso contrário.

# [DEFININDO FUNÇÃO] -----
# -- Função comparando string com lista
def verificar_lista(string, lista):
    # Definindo tipos de variáveis
    string = str(string)
    lista = list(lista)

    # Verificando se a stirng encontra-se dentro da lista
    if string in lista:
        return True
    else:
        return False


# [PROGRAMA PRINCIPAL] -----

# Iniciando variáveis
frutas = ["Maçã", "Pêra", "Abacate", 50, 30, 10]
texto = "maçã"

# Mostrando lista e texto
print(f"Lista: {frutas}")
print(f"Texto: {texto}")

# Mostrando resultado da verificação
print(f"O texto encontra-se na lista? {verificar_lista(texto, frutas)}")
