# Escreva uma função que receba uma string com as opções válidas a aceitar(cada opção é uma letra).
# Utilize o input para ler uma opção, converter o valor para letras minúsculas e verificar se a opção
# é válida. Em caso de opção inválida, a função deve pedir ao usuário que digite outra opção

# [DEFININDO FUNÇÃO] -----
# -- Função validador de opções
def transformar_string():
    # Definindo opções
    opções = ['minusculo', 'maiusculo', 'tamanho']

    # Recolhendo texto a ser transformado
    string = input("Digite o texto: ").strip()

    while True:
        # Mostrando opções disponíveis
        print("Escolha uma opção")
        print("[minusculo] | [maiusculo] | [tamanho]\n")

        # Recolhendo opção
        opção = str(input("Digite a opção: ").strip().lower())

        if opção == 'minusculo':
            return string.lower()

        elif opção == 'maiusculo':
            return string.upper()

        elif opção == 'tamanho':
            return len(string)

        else:
            print("OPÇÃO INVÁLIDA!\n")


# [PROGRAMA PRINCIPAL] -----

# Chamando função
print(transformar_string())
