# Modifique o exercíci anterior para receber o nom do arquivo ou diretório pela
# linha de comando. Imprima se existir e se for um arquivo ou um diretório
# OBS: ABRA ESTE ARQUIVO NO CMD

import sys
import os.path

# Iniciando variáveis
path = sys.argv[1]
diretorio = f"./Arquivos e diretórios/{path}"

# Verificando se existe o path inserido pelo usuário
if os.path.exists(diretorio):

    # Verificando o tipo do path
    if os.path.isdir(diretorio):
        tipo = "Diretório"

    if os.path.isfile(diretorio):
        tipo = "Arquivo"

    # Mensagem mostrando tipo do path
    print(f"{path} existe e é um {tipo}")

else:
    print(f"{path} não existe")
