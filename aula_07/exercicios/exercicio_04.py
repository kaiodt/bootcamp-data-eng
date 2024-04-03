##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 07 - Funções em Python e Estruturas de Dados - Parte 1                #
##############################################################################

# Exercício 04 ###############################################################
#                                                                            #
# Escreva uma função para converter uma lista de temperaturas em Celsius     #
# para Fahrenheit.                                                           #
#                                                                            #
##############################################################################

def celcius_to_fahrenheit(temperatures_in_celsius: list[float]) -> list[float]:
    return [32 + 9/5 * temp for temp in temperatures_in_celsius]

temperatures_in_celsius = [0, 100, 30, 20.5, 3.7]
print(celcius_to_fahrenheit(temperatures_in_celsius))
