##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 07 - Funções em Python e Estruturas de Dados - Parte 1                #
##############################################################################

# Exercício 03 ###############################################################
#                                                                            #
# Escreva uma função para contar valores únicos em uma lista.                #
#                                                                            #
##############################################################################

def count_unique_values(values: list[float]) -> int:
    return len(set(values))

values = [7, 1.3, 10, 10, 7]
print(count_unique_values(values))
