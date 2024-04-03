##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 07 - Funções em Python e Estruturas de Dados - Parte 1                #
##############################################################################

# Exercício 06 ###############################################################
#                                                                            #
# Escreva uma função para encontrar valores ausentes em uma sequência.       #
#                                                                            #
##############################################################################

def find_missing_values_in_sequence(values: list[int]) -> list[int]:
    full_sequence = range(min(values), max(values) + 1)
    return list(set(full_sequence) - set(values))

values = [15, 10, 13, 14, 17, 20, 19]
print(find_missing_values_in_sequence(values))
