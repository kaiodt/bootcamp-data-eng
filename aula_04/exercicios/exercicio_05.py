##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 05 ###############################################################
#                                                                            #
# * Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45,  #
#   "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de       #
#   compras.                                                                 #
#                                                                            #
##############################################################################

items = ["maçã", "banana", "cereja", "maçã"]

prices = {
    "maçã": 0.45,
    "banana": 0.30,
    "cereja": 0.65
}

total = sum(prices[item] for item in items if item.lower() in prices)

print(f"O total da lista de compras foi R$ {total:.2f}.")

