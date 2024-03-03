##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 13 - Fusão de Dicionários ########################################
#                                                                            #
# * Dado um dicionário de estoque de produtos, filtrar aqueles com           #
#   quantidade maior que 0.                                                  #
#                                                                            #
##############################################################################

stock = {
    "Teclado": 10,
    "Mouse": 0,
    "Monitor": 3,
    "CPU": 0
}

filt_stock = {
    product: quantity for product, quantity in stock.items() if quantity > 0
}

print(filt_stock)

