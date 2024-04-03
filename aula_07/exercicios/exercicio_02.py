##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 07 - Funções em Python e Estruturas de Dados - Parte 1                #
##############################################################################

# Exercício 02 ###############################################################
#                                                                            #
# Escreva uma função para filtrar dados acima de um limite.                  #
#                                                                            #
##############################################################################

def filter_above_limit(values: list[float], limit: float) -> list[float]:
    return [value for value in values if value > limit]

values = [5.7, 1.3, 3.75, 10, 7, 13]
print(filter_above_limit(values, limit=5))
