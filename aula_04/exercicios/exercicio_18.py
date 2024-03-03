##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 18 ###############################################################
#                                                                            #
# * Desenvolva uma função que receba uma string como argumento e retorne     #
#   essa string revertida.                                                   #
#                                                                            #
##############################################################################

def reverse_string(string: str) -> str:
    return string[::-1]

print(reverse_string("Hello, world!"))

