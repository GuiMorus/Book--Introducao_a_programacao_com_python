# Crie um programa que gere uma página HTML com links para todos os arquivos
# jpg e png encontrados a partir de um diretório informado na linha de comando

import sys
import os.path

# Iniciando variáveis
path = sys.argv[1]
diretorio = f'./Arquivos e diretórios/pagina HTML/{path}'
cont_arquivos = 0
imagens = []

# Listando tudo o que há dentro do path definido pelo usuário
lista = os.listdir(diretorio)

# Repetição recolhendo cara item dentro do diretório
for i in lista:
    if i.endswith(".png") or i.endswith(".jpg") or i.endswith(".jpeg"):
        cont_arquivos += 1      # Contando quantidade de imagens
        imagens.append(i)       # Recolhendo somendo arquivos com extensão .png ou .jpg

# Gerando Backup da página
with open('./Arquivos e diretórios/pagina HTML/backup.html', encoding='utf-8') as pagina:
    backup = pagina.read()

# Editando arquivo HTML com informações atualizadas
with open('./Arquivos e diretórios/pagina HTML/index.html', 'w', encoding='utf-8') as pagina:
    pagina.write(backup)    # Parte inicial do site

    # Montando restante do site
    pagina.write(f"""
    {diretorio}
    <h2>Imagens</h2>
    {cont_arquivos} imagens encontradas ao todo
    """)

    for i in imagens:
        # Gerando nome do arquivo sem o sufixo
        ponto = i.find('.')
        nome = i[0:ponto]

        pagina.write(f'\n<p><a href="{path}{i}">{nome}</a></p>')

    # Parte final do site
    pagina.write("""
    </body>
    </html>
    """)
