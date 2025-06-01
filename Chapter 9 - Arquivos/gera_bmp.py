# Cria um arquivo bmp a partir do desenho
ARQUIVO = "imagem_python.bmp"


def bytes_little_endian(numero, nbytes=4, sinal=False):
    """Converte um número inteiro para uma sequência de bytes usando
    a codificação little endian. Se o sinal for passado, reserva um bit para
    representar o sinal."""
    return numero.to_bytes(nbytes, "little", signed=sinal)


def padding(valor, tamanho=4):
    """Calcula o próximo múltiplo para o tamanho"""
    if resto := valor % tamanho:
        return valor + tamanho - resto
    return valor


# Tabela de conversão de letras para cor no formato
# RGB (red, green, blue) cada cor pode variar de 0 a 255.
letra_para_cor = {
    " ": (0, 0, 0),         # Preto
    "r": (255, 0, 0),       # Vermelho
    "g": (0, 255, 0),       # Verde
    "b": (0, 0, 255),       # Azul
}

# Desenho que vamos transformar em imagem
desenho = [
    " rrrr r r bbbbb b    b  ggggg  g    g r ",
    " r  r r r   b   b    b g     g gg   g r ",
    " r  r r r   b   b    b g r r g g g  g r ",
    " rrr   r    b   bbbbbb g     g g  g g r ",
    " r     r    b   b    b gr b rg g  g g r ",
    " r     r    b   b    b g rrr g g   gg   ",
    " r     r    b   b    b  ggggg  g    g r "
]

# Multiplicador de pontos
# Cada ponto será copiado multiplicado x vezes na imagem
# Se for igual a 4, cada ponto gera um bloco de 4x4 pontos
multiplicador = 32

# Checa se todas as linhas têm o mesmo tamanho
largura_desenho = len(desenho[0])
for linha, z in enumerate(desenho):
    if len(z) != largura_desenho:
        raise ValueError(f"""linhas devem ter o mesmo tamanho.
        Linha com largura diferente: {linha} em vez de {len(z)}""")

# Calcula os dados com base no multiplicador
desenho_expandido = []
for linha in desenho:
    nova_linha = []
    for letra in linha:
        nova_linha.append(letra * multiplicador)
    for _ in range(multiplicador):
        desenho_expandido.append("".join(nova_linha))

largura = len(desenho_expandido[0])     # Número de colunas na imagem
altura = len(desenho_expandido)         # Número de linhas na imagem

# Checa se as letras representam as cores
dados_binarios = []
for linha in desenho_expandido:
    linha_binaria = []
    for caractere in linha:
        linha_binaria.append(bytes(letra_para_cor[caractere]))
    dados_binarios.append(b"".join(linha_binaria))

# Adiciona o padding
largura_bytes = largura * 3
largura_com_padding = padding(largura_bytes)
if largura_bytes != largura_com_padding:
    for p, d in enumerate(dados_binarios):
        dados_binarios[p] = b"".join([dados_binarios[p], bytes(largura_com_padding - largura_bytes)])

# Calcula o tamanho em bytes da imagem com o padding
tamanho = padding(largura * 3) * altura

cabeçalho_bmp = [
    b"BM",                                  # Identificador
    bytes_little_endian(54 + tamanho),      # Tamanho da imagem em bytes
    bytes(4),                               # 4 bytes 0x00
    bytes_little_endian(54)                 # Tamanho dos cabeçalhos
]

cabeçalho_dib = [
    bytes_little_endian(40),                    # Tamanho do cabeçalho DIB
    bytes_little_endian(largura),               #
    bytes_little_endian(-altura, sinal=True),   # Altura negativa para montar a imagem de cima para baixo
    bytes_little_endian(1, 2),    # Planos de cor
    bytes_little_endian(24, 2),   # Bits por ponto
    bytes_little_endian(0),                     # Sem compressão
    bytes_little_endian(tamanho),               #
    bytes_little_endian(2835),                  # Teto(72 dpi x 39.3701 pol/m) horizontal
    bytes_little_endian(2835),                  # Teto(72 dpi x 39.3701 pol/m) vertical
    bytes_little_endian(0),                     # Número de cores na paleta
    bytes_little_endian(0)                      # Cores Importantes
]

cabeçalho_bmp_binario = b"".join(cabeçalho_bmp)
cabeçalho_dib_binario = b"".join(cabeçalho_dib)
dados_binarios = b"".join(dados_binarios)

# Verifica o tamanho de cada cabeçalho binário
assert len(cabeçalho_bmp_binario) == 14
assert len(cabeçalho_dib_binario) == 40
assert len(dados_binarios) == tamanho

# Grava a imagem
with open(ARQUIVO, "wb") as image:
    image.write(cabeçalho_bmp_binario)
    image.write(cabeçalho_dib_binario)
    image.write(dados_binarios)

print(f"Arquivo {ARQUIVO} gerado. {largura=} x {altura=} tamanho: {tamanho=} bytes")
