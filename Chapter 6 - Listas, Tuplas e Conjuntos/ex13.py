# A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista
# T = [-10, -8, 0, 1, 2, 5, -2, -4]. Faça um prgrama que imprima a menor e a maior
# temperatura, assim como a temperatura média.

# Iniciando variável
T = [-10, -8, 0, 1, 2, 5, -2, -4]

# Calculando média
media = sum(T) / len(T)

# Repetição definindo maior e menor
maior = media
menor = media

for i in T:
    # Verificação do maior
    if i > maior:
        maior = i

    # Verificação do menor
    if i < menor:
        menor = i

# Mostrando resultado
print(f"Temperatura = {T}")
print(f"Média da temperatura: {media}")
print(f"Maior temperatura: {maior}")
print(f"Menor temperatura: {menor}")
