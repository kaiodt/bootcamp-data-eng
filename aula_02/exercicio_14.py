##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 02 - TypeError, Type Check, Type Conversion, try-except e if          #
##############################################################################

# Exercício 14 ###############################################################
#                                                                            #
# Faça um programa que peça ao usuário para digitar uma data no formato      #
# "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.    #
#                                                                            #
##############################################################################

date = input("Digite uma data no formato 'dd/mm/aaaa': ")
day, month, year = date.split("/")

print(f"Dia: {day}")
print(f"Mês: {month}")
print(f"Ano: {year}")

