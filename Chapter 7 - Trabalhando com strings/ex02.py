# Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns
# às duas strings lidas.
#
# 1º string: AAACTBF
# 2° string: CBT
# resultado: CBT
# Obs: a ordem dos caracteres da string gerada não é importante, mas deve conter todas
# as letras comuns a ambas.

# Iniciando variáveis
primeira = "AAACTBF"
segunda = "CBT"

# Gerando lista com a intesecção das strings
conjunto = set(primeira) & set(segunda)
terceiro = "".join(conjunto)

# Mostrando resultado
print(f"1° String: {primeira}")
print(f"2° String: {segunda}")
print(f"3° String intersecção: {terceiro}")
