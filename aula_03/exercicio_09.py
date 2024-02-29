##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Exercício 09 - Extração de Subconjuntos de Dados ###########################
#                                                                            #
# * Dada uma lista de números, extrair apenas aqueles que são pares.         #
#                                                                            #
##############################################################################

numbers = range(1, 11)

even_numbers = [n for n in numbers if n % 2 == 0]

print(f"Lista original: {numbers}")
print(f"Lista somente com pares: {even_numbers}")

