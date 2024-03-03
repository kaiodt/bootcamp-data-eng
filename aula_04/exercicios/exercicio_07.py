##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 07 - Filtragem de Dados ##########################################
#                                                                            #
# * Dada uma lista de idades, filtrar apenas aquelas que são maiores ou      #
#   iguais a 18.                                                             #
#                                                                            #
##############################################################################

ages = [22, 15, 30, 17, 18]

filt_ages = [age for age in ages if age >= 18]

print(f"Idades iguais ou maiores que 18: {filt_ages}.")

