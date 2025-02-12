# Crie um programa que leia um arquivo-texto e gere um arquivo de saída paginado. Cada
# linha não deve conter mais que 76 caracteres. Cada página terá no máximo 60 linhas.
# Adicione na última linha de cada página o número da página atual e o nome do arquivo original

# Iniciando variáveis
arquivo_original = 'arquivo-texto.txt'
limite_char = 76
limite_linhas = 60
page = 1
resto = ''


# --Função Quebrando texto
def quebrarlinha(_linha, _limite, _lista=None):

    if _lista is None:
        _lista = []
    if len(_linha) >= _limite:
        _lista.append(_linha[:_limite])
        return quebrarlinha(_linha[_limite:], _limite, _lista)

    _lista.append(_linha)
    return _lista


# Abrindo arquivo com texto
with open(arquivo_original, encoding='utf-8') as arquivo:

    linha_atual = 1         # contador da linha

    # Lendo linhas do arquivo
    for linha in arquivo.readlines():

        # Verificando linha atual
        if linha_atual >= limite_linhas:

            page += 1           # Atualizando número da página
            linha_atual = 1     # Reiniciando contador

        # Atualizando nome da página
        pagina = f"pagina-{page}.txt"

        with open(pagina, 'a', encoding='utf-8') as arquivo_pagina:

            # Resgatando lista com limite de linhas
            lista = quebrarlinha(linha, limite_char)

            # Repetição para escrever as linhas quebradas em lista
            fim = len(lista)
            for i in range(0, fim):

                # Formatando informação
                item = str(lista[i]).strip()

                # Escrevendo conteúdo na página atual
                arquivo_pagina.write(item + '\n')
                linha_atual += 1

                # Verificando linha final
                if linha_atual >= limite_linhas:

                    arquivo_pagina.write(f"\nPágina: {page} \n")
                    arquivo_pagina.write(f"Arquivo: {arquivo_original}")

    # Colocando número da página e nome do arquivo na última página
    with open(pagina, 'a', encoding='utf-8') as arquivo_pagina:

        arquivo_pagina.write(f"\nPágina: {page} \n")
        arquivo_pagina.write(f"Arquivo: {arquivo_original}")
