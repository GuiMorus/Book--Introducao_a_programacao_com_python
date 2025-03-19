# Modifique o programa anterior para que leia o mesmo arquivo, permitindo adicionar
# mais dados ao arquivo. Se o mesmo nome for digitado duas vezes, altere os
# dados da nova entrada.

import json

# Iniciando variáveis
diretorio = './Arquivos de texto/notas.json'
cont = 0

# Lendo arquivo JSON
with open(diretorio, encoding='utf-8') as arquivo:
    # Colocando dados do arquivo dentro de uma variável
    cadastro = json.load(arquivo)

# Loop do menu principal
while True:

    # Corpo inicial
    print("-" * 15, "MENU DE CADASTRO", "-" * 15)
    print("[ 1 ] - Novo Cadastro")
    print("[ 2 ] - Ler dados")
    print("[ 3 ] - Sair")
    opção = int(input("Opção: ").strip())

    # Novo cadastro de aluno
    if opção == 1:
        print("\n[NOVO CADASTRO]")
        nome = input("Nome do aluno(a): ").strip().title()
        nota1 = int(input("Digita a 1° nota: ").strip().replace(',', '.'))
        nota2 = int(input("Digita a 2° nota: ").strip().replace(',', '.'))
        nota3 = int(input("Digita a 3° nota: ").strip().replace(',', '.'))
        nota4 = int(input("Digita a 4° nota: ").strip().replace(',', '.'))
        media = (nota1 + nota2 + nota3 + nota4) / 4

        # Verificando nome existente do aluno
        for i in cadastro:
            cont += 1
            if i['nome'] == nome:
                # Atualizando informações
                i['nota1'] = nota1
                i['nota2'] = nota2
                i['nota3'] = nota3
                i['nota4'] = nota4
                i['media'] = media
                break

            # Cadastrando novo aluno(a)
            elif cont >= len(cadastro):
                cont = 0  # Reiniciando contagem
                cadastro.append({'nome': nome, 'nota1': nota1,
                                 'nota2': nota2, 'nota3': nota3,
                                 'nota4': nota4, 'media': media
                                 })

        # Mensagem de atualização de dados
        print("Deseja atualizar o banco de dados?")
        print("[ S ] - Sim")
        print("[ N ] - Não")
        atualizar = input("Opção: ").strip().upper()

        # Verificando opção escolhida pelo usuário
        if atualizar == 'S' or "SIM":
            # Atualizando arquivo JSON
            with open(diretorio, 'w', encoding='utf-8') as arquivo:
                json.dump(cadastro, arquivo, indent=2, ensure_ascii=False)
