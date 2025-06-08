# Crie classes para representar estados e cidades.
# Cada estado têm: nome, sigla e cidade.
# Cada cidade têm: nome e população.
# Escreva um programa de testes que crie até três estados com algumas cidades em cada um
# Exiba a população de cada estado como a soma da população de suas cidades

from cidades import Cidade
from estados import Estado

# Declarando objtos
sãoPaulo = Estado("São Paulo", "SP")
minasGerais = Estado("Minas Gerais", "MG")
rioDeJaneiro = Estado("Rio de Janeiro", "RJ")

osasco = Cidade("Osasco", 728_615)
itapevi = Cidade("Itapevi", 232_297)
jundiai = Cidade("Jundiaí", 443_221)
ouroPreto = Cidade("Ouro Preto", 74_824)
diamantinha = Cidade("Diamantina", 47_702)
beloHorizonte = Cidade("Belo Horizonte", 2_315_560)
petrópolis = Cidade("Petóprolis", 278_881)
teresópolis = Cidade("Teresópolis", 165_123)
búzios = Cidade("Búzios", 40_006)

# Adicionando cidades em cada estado
sãoPaulo.inserir_cidade(osasco)
sãoPaulo.inserir_cidade(itapevi)
sãoPaulo.inserir_cidade(jundiai)
minasGerais.inserir_cidade(ouroPreto)
minasGerais.inserir_cidade(diamantinha)
minasGerais.inserir_cidade(beloHorizonte)
rioDeJaneiro.inserir_cidade(petrópolis)
rioDeJaneiro.inserir_cidade(teresópolis)
rioDeJaneiro.inserir_cidade(búzios)

# Mostrando total de habitantes de cada estado
sãoPaulo.mostrar_habitantes()
minasGerais.mostrar_habitantes()
rioDeJaneiro.mostrar_habitantes()
