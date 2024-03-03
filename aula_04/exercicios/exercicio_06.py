##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 06 - Eliminação de Duplicatas ####################################
#                                                                            #
# * Dada uma lista de emails, remover todos os duplicados.                   #
#                                                                            #
##############################################################################

emails = [
    "user@example.com", "admin@example.com", "user@example.com",
    "manager@example.com"
]

# Convertendo a lista para conjunto (set) e voltando para lista.
# A conversão para conjunto automatiamente remove as duplicatas.
unique_emails = list(set(emails))

print(unique_emails)

