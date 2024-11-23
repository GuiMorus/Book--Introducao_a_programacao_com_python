# Escreva uma função para validar uma variável string. Essa função recebe como
# parâmetro a string, o númerio mínimo e máximo de caracteres. Retorne verdadeiro se
# o tamanho da string estiver entre os valores de máximo e mínimo, e falso, caso contrário.

# [DEFININDO FUNÇÃO] -----
# -- Função validadora de string
def verificar_tamanho(string, maximo, minimo=2):
    # Recolhendo tamanho da string
    tamanho = len(string)

    # Verificando string dentro do intervalo
    if maximo >= tamanho >= minimo:
        return True
    else:
        return False


# [PROGRAMA PRINCIPAL] -----
texto = "Piracicaba"

print(f"O texto: {texto} está dentro do intervalo: {verificar_tamanho(texto, 10)}")
