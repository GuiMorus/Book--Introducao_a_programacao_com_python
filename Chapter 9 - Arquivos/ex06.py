# Modifique o exercício anterior para imprimir 40 vezes o símbolo de = se esse
# for o primeiro caractere da linha. Adcione também a opção para parar de imprimir
# até que se pressione a tecla ENTER cada vez que uma linha iniciar com . (ponto)
# como primeiro caractere.

# Iniciando varáveis
continuar = True
opção = '1'

# Loop principal
while continuar:

    # Abrindo arquivo para leitura
    with open('Arquivos de texto/entrada2.txt', encoding='utf-8') as arquivo:
        # Repetição lendo cara linha do arquivo
        for linha in arquivo.readlines():

            # Verificando símbolo da linha
            if linha[0] == '=':
                print("=" * 40)     # Criando símbolo repetido

            # Verificando símbolo da linha
            elif linha[0] == '.':
                print("Aperte ENTER para parar ou 1 para continuar")
                opção = input("Opção: ").strip()

            # Verificando continuidade
            if opção == '':
                continuar = False
                break
