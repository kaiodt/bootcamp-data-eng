##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 10 - Divisão de Dados em Grupos ##################################
#                                                                            #
# * Dada uma lista de valores, dividir em duas listas: uma para valores      #
#   pares e outra para ímpares.                                              #
#                                                                            #
##############################################################################

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [value for value in values if value % 2 == 0]
odd = [value for value in values if value % 2 != 0]

print(f"Valores pares: {even}")
print(f"Valores ímpares: {odd}")

