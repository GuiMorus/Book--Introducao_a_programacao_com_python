# Escreva um programa que leia um número e verifique se é ou não um número primo.

# Introdução
print("-" * 10, "É PRIMO?", "-" * 10)

# Lendo valor para verificá-lo
num = int(input("Digite o número: "))

# Verificando se o número é primo
primo = True
for c in range(2, num - 1):

    # Testando se o número é divisível entre 1 e o próprio número
    if num % c == 0:
        primo = False

# Mostrando resultado
resultado = "é primo" if primo else "não é primo"
print(f"O número {num} {resultado}")
