# Altere o Programa6.py para exibir o tamanho da agenda no menu principal

# Execute o programa a seguir e analise-o cuidadosamente
# Programa 6: Controle de uma agenda de telefones

# Iniciando variável
agenda = []


# --Função registrar nome
def pede_nome():
    return input("Nome: ")


# --Função registrar telefone
def pede_telefone():
    return input("Telefone: ")


# --Função para mostrar os dados
def mostra_dados(nome, telefone):
    print(f"Nome: {nome} Telefone: {telefone}")


# --Função resgatando o nome do arquivo
def pede_nome_arquivo():
    return input("Nome do arquivo: ")


# --Função pesquisar usuário
def pesquisa(nome):
    # Colocando nome em minúsculo
    mnome = nome.lower()

    # Repetição verificando se há o usuário | i = indice | v = valor
    for i, v in enumerate(agenda):
        # Condição buscando pelo nome
        if v[0].lower() == mnome:
            return i  # Retornando o indice dentro da lista agenda

    # Retornando nada caso não encontre o usuário
    return None


# --Função novo usuário
def novo():
    nome = pede_nome()  # Recolhendo nome do usuário
    telefone = pede_telefone()  # Recolhendo telefone do usuário
    agenda.append([nome, telefone])  # Registrando informações na agenda


# --Função apagar usuário
def apaga():
    nome = pede_nome()  # Recolhendo nome do usuário
    indice = pesquisa(nome)  # Pesquisando se há o usuário na agenda

    # Condição verificando se foi retornado o indice do usuário
    if indice is not None:

        # Apagando usuário
        del agenda[indice]

    else:
        print("Nome não encontrado")


# --Função alterar dados do usuário
def altera():
    # Recolhendo indice com base no nome
    indice = pesquisa(pede_nome())

    # Condição verificando se foi retornado o indice do usuário
    if indice is not None:

        nome = agenda[indice][0]  # Recolhendo nome dentro da agenda
        telefone = agenda[indice][1]  # Recolhendo telefone dentro da agenda
        print("Usuário encontrado:")  # Mostrando mensagem

        mostra_dados(nome, telefone)  # Mostrando os dados do usuário
        nome = pede_nome()  # Recolhendo NOVO nome do usuário
        telefone = pede_telefone()  # Recolhendo NOVO telefone do usuário
        agenda[indice] = [nome, telefone]  # Atualizando agenda com base no indice

    else:
        print("Nome não encontrado")


# --Função mostrando a agenda
def lista():
    print("\nAgenda \n\n-------")  # Mostrando mensagem

    # Repetição recolhendo itens da agenda
    for i in agenda:
        mostra_dados(i[0], i[1])

    print("-------\n")  # Mensagem final


# --Função lendo arquivo existente
def ler():
    global agenda  # Modificando variável (lista) agenda
    nome_arquivo = pede_nome_arquivo()  # Recolhendo nome do arquivo

    # Abrindo arquivo existente
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        # Reiniciando agenda
        agenda = []

        # Repetição recolhendo informações dos usuários linha por linha
        for linha in arquivo.readlines():
            nome, telefone = linha.strip().split('#')  # Recolhendo informações separados por: #
            agenda.append([nome, telefone])  # Inserindo dados do usuário na agenda


# --Função gravar arquivo com informações da agenda
def gravar():
    nome_arquivo = pede_nome_arquivo()

    with open(nome_arquivo, 'a', encoding="utf-8") as arquivo:
        for i in agenda:
            linha = f"{i[0]}#{i[1]}\n"
            arquivo.write(linha)


# --Função validador das opções
def validar_faixa(pergunta, inicio, fim):
    # Loop para recolher a opção correta
    while True:

        # Tratamento de erro do valor
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor

        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")


# --Função mostrando o menu
def menu():
    # Introdução
    print("-" * 15, "AGENDA DE USUÁRIOS", "-" * 15)
    print(f"Total de usuários: {len(agenda)}")

    # Opções
    print("""
    1 - Novo
    2 - Alterar
    3 - Apagar
    4 - Listar
    5 - Gravar
    6 - Ler

    0 - Sair
    """)

    return validar_faixa("Escolha uma opção: ", 0, 6)


# ---- PROGRAMA PRINCIPAL ---- #
while opção := menu():

    # Sair do programa
    if opção == 0:
        break

    # Criar novo usuário
    elif opção == 1:
        novo()

    # Alterar um usuário existente
    elif opção == 2:
        altera()

    # Apagar um usuário
    elif opção == 3:
        apaga()

    # Listar os usuários da agenda
    elif opção == 4:
        lista()

    # Gerar um arquivo gravando as informações dos usuários
    elif opção == 5:
        gravar()

    # Ler um arquivo de usuários existente
    elif opção == 6:
        ler()
