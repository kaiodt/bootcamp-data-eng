##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 07 - Funções em Python e Estruturas de Dados - Parte 1                #
##############################################################################

# Exercício 01 ###############################################################
#                                                                            #
# Escreva uma função para calcular média de valores em uma lista.            #
#                                                                            #
##############################################################################

def compute_mean(values: list[float]) -> float:
    return sum(values) / len(values)

values = [5.7, 1.3, 3.75, 10, 7, 13]
print(compute_mean(values))
