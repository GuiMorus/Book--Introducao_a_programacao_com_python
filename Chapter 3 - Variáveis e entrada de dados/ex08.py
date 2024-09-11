# Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

# Resgatando o valor em metros digitado pelo usuário
print("=" * 10, "CONVERSOR DE METROS EM MILÍMETROS", "=" * 10)  # Introdução

metro = input("Digite a quantidade de Metros: ")
metro = float(metro.replace(',', '.').strip())      # Tratando o dado

# Convertendo e mostrando o resultado
print(f"Milímetros: {metro * 1000}")
print("=" * 55)     # Encerramento
