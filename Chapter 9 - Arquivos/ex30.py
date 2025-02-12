# Modifique o Programa 8 para gerar uma lista html, usando os elementos <ul> e <il>
# Todos os elementos da lista devem estar dentro do elemento <ul>, e cada item
# dentro de um elemento <li>

# Iniciando variável
filmes = {
    "drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "comédia": ["Tempos Modernos", "American Pie", "Dr. Dollitle"],
    "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
    "guerra": ["Rambo", "Platoon", "Tora!Tora!Tora!"]
}

# Escrevendo arquivo HTML
diretorio = "./Arquivos de texto/"
with open(f"{diretorio}filmes.html", 'w', encoding='utf-8') as pagina:
    # Bloco HTML inicial
    pagina.write("""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Filmes 🐍</title>
    </head>
    <body>
    """)

    # Repetição ordenando os itens em H1 e H2 | c = chave | v = valor
    for c, v in filmes.items():
        # Escrevendo título
        pagina.write(f"<h1>{c.title()}</h1>\n")
        pagina.write("<ul>\n")

        # Repetição para escrever os itens
        for i in v:
            pagina.write(f"<li>{i}</li>\n")

        pagina.write("</ul>\n")

    # Bloco HTML final
    pagina.write("""
    </body>
    </html>
    """)

