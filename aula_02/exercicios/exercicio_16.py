##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 02 - TypeError, Type Check, Type Conversion, try-except e if          #
##############################################################################

# Exercício 16 ###############################################################
#                                                                            #
# Escreva um programa que avalie duas expressões booleanas inseridas pelo    #
# usuário e retorne o resultado da operação AND entre elas.                  #
#                                                                            #
##############################################################################

val_1 = bool(input("Digite verdadeiro ('True') ou falso (''): "))
val_2 = bool(input("Digite verdadeiro ('True') ou falso (''): "))

print(f"{val_1} AND {val_2} = {val_1 and val_2}")

