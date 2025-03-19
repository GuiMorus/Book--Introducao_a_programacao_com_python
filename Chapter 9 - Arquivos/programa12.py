# árvore de diretórios sendo percorrida

import os

# Repetição percorrendo os diretórios
for raiz, diretórios, arquivos in os.walk(".\\"):
    # Mostrando raiz
    print("\033[32m", f"Caminho: {raiz}", "\033[m")

    # Mostrando diretórios
    for i in diretórios:
        print("\033[33m", f"   {i}/", "\033[m")

    # Mostrando arquivos
    for i in arquivos:
        print(f"    {i}")
