##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Exercício 07 - Normalização de Dados #######################################
#                                                                            #
# * Normalizar uma lista de números para que fiquem na escala de 0 a 1.      #
#                                                                            #
##############################################################################

numbers = [10, 20, 30, 40, 50]
max_number = max(numbers)
min_number = min(numbers)

norm_numbers = [
    (n - min_number) / (max_number - min_number) for n in numbers
]

print(f"Lista original: {numbers}")
print(f"Lista normalizada: {norm_numbers}")

