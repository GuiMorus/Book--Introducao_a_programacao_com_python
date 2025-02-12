# Processamento de um arquivo
LARGURA = 79

# Abrindo arquivo com as entradas
with open('Arquivos de texto/entrada.txt', encoding='utf-8') as entrada:

    # Repetição lendo linha a linha
    for linha in entrada.readlines():

        # Verificando se a linha começa com um símbolo específico
        if linha[0] == ';':
            # Continuando
            continue

        # Verificando se a linha começa com outro símbolo específico
        elif linha[0] == '>':

            # Mostrando tratamento da mensagem
            print(linha[2:].rjust(LARGURA))

        # Verificando se a linha começa com outro símbolo específico
        elif linha[0] == "*":
            print(linha[2:].center(LARGURA))

        # Mostrando linha normalmente caso não tenha os símbolos acima
        else:
            print(linha)
