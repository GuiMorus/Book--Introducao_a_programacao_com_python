# Escreva uma função que receba a base e a altura de um triângulo e retorne sua área
# (A = (base x altura) / 2)

# DEFININDO FUNÇÃO
# -- Função calculando área de um triângulo
def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


# --- PROGRAMA PRINCIPAL --- #

# Mostrando resultado das áreas dos triângulos
print(area_triangulo(6, 9))
print(area_triangulo(5, 8))
