##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 07 - Funções em Python e Estruturas de Dados - Parte 1                #
##############################################################################

# Exercício 05 ###############################################################
#                                                                            #
# Escreva uma função para calcular o desvio padrão dos valores de lista.     #
#                                                                            #
##############################################################################

def compute_standard_deviation(values: list[float]) -> float:
    mean = sum(values) / len(values)
    variance = sum((x - mean)**2 for x in values) / len(values)
    return variance ** 0.5

values = [5.7, 1.3, 3.75, 10, 7, 13]
print(compute_standard_deviation(values))
