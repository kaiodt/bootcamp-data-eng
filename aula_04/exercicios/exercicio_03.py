##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 03 ###############################################################
#                                                                            #
# * Crie um dicionário para armazenar informações de um livro, incluindo     #
#   título, autor e ano de publicação. Imprima cada informação.              #
#                                                                            #
##############################################################################

book = {
    "Título": "Guia do Mochileiro das Galáxias",
    "Autor": "Douglas Adams",
    "Ano de Publicação": 1979,
}

for key, value in book.items():
    print(f"{key}: {value}")

