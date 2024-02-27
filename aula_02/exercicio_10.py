##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 02 - TypeError, Type Check, Type Conversion, try-except e if          #
##############################################################################

# Exercício 10 ###############################################################
#                                                                            #
# Escreva um programa que calcule a área de um círculo, recebendo o raio     #
# como entrada.                                                              #
#                                                                            #
##############################################################################

from math import pi

radius = float(input("Digite o raio do círculo: "))

print(f"A área do círculo de raio {radius} é {pi * (radius ** 2):.3f}")

