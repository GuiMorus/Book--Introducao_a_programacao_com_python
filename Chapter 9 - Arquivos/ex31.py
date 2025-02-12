# Crie um programa que verifique se existe um diretório e mostre o tipo dele

import os.path

# Iniciando variáveis
path = 'c'
diretorio = f'./Arquivos e diretórios/{path}'

# Verificando se z existe
if os.path.exists(diretorio):

    # Verificando se é um diretório ou arquivo
    if os.path.isfile(diretorio):
        tipo = "Arquivo"

    if os.path.isdir(diretorio):
        tipo = "Diretório"

    # Mensagem do tipo
    print(f"{path} existe e é um {tipo}")

else:
    print(f"{path} não existe")
