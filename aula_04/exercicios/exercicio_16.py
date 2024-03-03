##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 16 ###############################################################
#                                                                            #
# * Escreva uma função que receba uma lista de números e retorne a soma de   #
#   todos os números.                                                        #
#                                                                            #
##############################################################################

def sum_values(values: list[int | float]) -> int | float:
    total = 0
    for value in values:
        total += value
    
    return total

values = [64, 34, 25, 12, 22, 11, 90]

print(f"A soma dos valores é {sum_values(values)}.")

