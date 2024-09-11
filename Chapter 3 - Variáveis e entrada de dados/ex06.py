# Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado.
# Para ser aprovado, todas as médias do aluno devem ser maiores ou iguais a 7.
# Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está
# armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.

# Recuperando as notas do aluno
print("=" * 10, " APROVAÇÃO ", "=" * 10)
matéria1 = float(input("Nota da 1° Matéria: ").replace(',', '.').strip())
matéria2 = float(input("Nota da 2° Matéria: ").replace(',', '.').strip())
matéria3 = float(input("Nota da 3° Matéria: ").replace(',', '.').strip())

media = (matéria1 + matéria2 + matéria3) / 3

# Verificando e mostrando aprovação
aprovado = media >= 7
print()     # pulando linha

if aprovado:
    print("PARABÉNS FOI APROVADO!!!")
else:
    print("Você reprovou :(")

# Mensagem final
print("=" * 33)
