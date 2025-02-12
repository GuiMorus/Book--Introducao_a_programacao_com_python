# Crie um programa que receba uma lista de nomes de arquivo e os imprima, um por um

# Iniciando variável
arquivos = []

# Loop recolhendo o nome dos arquivos
while True:

    # Recolhendo nome do arquivo
    print("\nPara finalizar digite: sair")
    nome = input("Nome do arquivo: ")

    # Verificando saída
    if nome in "Sair sair":
        break
    else:

        # Verificando se há a extensão .txt ao final
        if not nome.endswith('.txt'):
            nome = f"{nome}.txt"

        # Cadastrando nome do arquivo na lista
        arquivos.append(nome.strip())

# Verificando se há arquivos digitados
if len(arquivos) > 0:

    # Repetição lendo cada arquivo inserido
    for doc in arquivos:

        # Nome do arquivo
        print("\n\033[32m" + f"ARQUIVO ATUAL: {doc}" + "\033[m")

        # Abrindo documentos em modo leitura
        with open(doc, 'r', encoding='utf-8') as arquivo:

            # Lendo arquivo linha por linha
            for linha in arquivo.readlines():

                print(linha, end='')    # Imprimendo texto

        # Final do arquivo
        print("\033[31m" + "-- FIM --" + "\033[m")
        print()

else:

    # Mensagem de arquivos vazios
    print("NÃO HÁ ARQUIVOS")
