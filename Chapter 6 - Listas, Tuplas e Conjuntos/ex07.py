# Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os
# parênteses foram abertos e fechados na ordem correta.
#
# Você pode adicionar elementos à pilha sempre que encontrar um "abre parênteses" e
# desempilhá-la a cada "fecha parênteses". Se a expressão estiver correta, sua pilha
# estará vazia no final

# Iniciando variável
pilha = []

# Recolhendo expressão do usuário
leitura = input("Digite a expressão: ").strip()

# Repetição percorrendo a String de leitura
for i in leitura:

    # Verificando abertura de parênteses
    if i == "(":
        pilha.append(i)     # Adicionando à pilha

    elif i == ")":

        # Verificando se a pilha não está vazia
        if len(pilha) > 0:
            pilha.pop(-1)       # Removendo da pilha

        else:
            pilha.append(i)     # Adicionando a pilha caso ela seja vazia

# Mostrando resultado
resultado = "CORRETA!" if len(pilha) == 0 else "ERRADA :("
print(f"Sua expressão está {resultado}")
