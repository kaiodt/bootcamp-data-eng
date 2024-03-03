##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 11 - Atualização de Dados ########################################
#                                                                            #
# * Dada uma lista de dicionários representando produtos, atualizar o preço  #
#   de um produto específico.                                                #
#                                                                            #
##############################################################################

products = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

# Atualizar produto com id = 2
for product in products:
    if product["id"] == 2:
        product["preço"] = 90

print(products)

