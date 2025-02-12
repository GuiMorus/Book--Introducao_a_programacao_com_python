# Lendo o arquivo números.txt gerado no exercício anterior

# Abrindo arquivo
arquivo = open("Arquivos de texto/números.txt", 'r')

# Repetição para exibir as linhas do arquivo
for linha in arquivo.readlines():
    print(linha, end="")

# Fechando arquivo
arquivo.close()
