# Reescreva a função do Programa 8.1 de forma a utilizar os métodos de pesquisa em lista,
# vistos no Capítulo 7.

# DEFININDO FUNÇÃO
# -- Função pesquisando índice
def pesquisa_indice(lista, valor):
    # Verificando se há o valor dentro da lista
    if valor in lista:
        # Retornando o indice do valor
        return lista.index(valor)

    # Retornando valor nulo caso não encontre o valor dentro da lista
    return None


numeros = [5, 7, 8, 10]
palavras = ['Abacaxi', 'Tempero', 'maçã', 'Maçã']

print(f"O índice retornado foi: {pesquisa_indice(numeros, 9)}")
print(f"O índice retornado foi: {pesquisa_indice(palavras, 'Maçã')}")
