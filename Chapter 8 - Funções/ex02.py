# Escreva uma função que receba dois números e retorne True se o primeiro for múltiplo do segundo.

# DEFININDO FUNÇÃO
# -- Função verificando multiplo
def multiplo(a, b):
    if a % b == 0:
        return True
    else:
        return False


# --- PROGRAMA PRINCIPAL --- #

# Mostrando resultado dos valores utilizando função multiplo
print(multiplo(8, 4))
print(multiplo(7, 3))
print(multiplo(5, 5))
