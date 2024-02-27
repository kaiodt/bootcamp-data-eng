##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 02 - TypeError, Type Check, Type Conversion, try-except e if          #
##############################################################################

# Exercício 17 ###############################################################
#                                                                            #
# Crie um programa que receba dois valores booleanos do usuário e retorne o  #
# resultado da operação OR.                                                  #
#                                                                            #
##############################################################################

val_1 = bool(input("Digite verdadeiro ('True') ou falso (''): "))
val_2 = bool(input("Digite verdadeiro ('True') ou falso (''): "))

print(f"{val_1} OR {val_2} = {val_1 or val_2}")

