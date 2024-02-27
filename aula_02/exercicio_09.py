##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 02 - TypeError, Type Check, Type Conversion, try-except e if          #
##############################################################################

# Exercício 09 ###############################################################
#                                                                            #
# Faça um programa que converta a temperatura de Celsius para Fahrenheit.    #
#                                                                            #
##############################################################################

temp_C = float(input("Digite a temperatura em Celcius: "))
temp_F = 32 + (temp_C * 9/5)

print(f"{temp_C} °C = {temp_F} °F")

