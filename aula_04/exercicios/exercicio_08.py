##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 08 - Ordenação Personalizada #####################################
#                                                                            #
# * Dada uma lista de dicionários representando pessoas, ordená-las pelo     #
#   nome.                                                                    #
#                                                                            #
##############################################################################

people = [
    {"nome": "Douglas", "idade": 30},
    {"nome": "Carol", "idade": 20},
    {"nome": "Bob", "idade": 25},
    {"nome": "Alice", "idade": 20},
]

people_sorted = sorted(people, key=lambda p: p["nome"])

print(people_sorted)

