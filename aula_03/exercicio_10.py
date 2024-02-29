##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Exercício 10 - Agregação de Dados por Categoria ############################
#                                                                            #
# * Dado um conjunto de registros de vendas, calcular o total de vendas por  #
#   categoria.                                                               #
#                                                                            #
##############################################################################

sales = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800},
    {"categoria": "roupas", "valor": 80},
    {"categoria": "livros", "valor": 60},
]

sales_by_category = {}

for sale in sales:
    cat, value = sale["categoria"], sale["valor"]
    sales_by_category[cat] = sales_by_category.get(cat, 0) + value

print(sales_by_category)

