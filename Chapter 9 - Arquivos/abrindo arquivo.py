# Escrevendo numeros de 1 a 100 em arquivo txt utilizando o python

# Abrindo arquivo
arquivo = open("Arquivos de texto/números.txt", "w")

# Repetição escrevendo dentro do arquivo
for linha in range(1, 101):
    # Escrevendo dentro do arquivo
    arquivo.write(f"{linha}\n")

# Fechando o arquivo
arquivo.close()
