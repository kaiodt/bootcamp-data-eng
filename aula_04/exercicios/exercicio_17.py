##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 17 ###############################################################
#                                                                            #
# * Crie uma função que receba um número como argumento e retorne `True` se  #
#   o número for primo e `False` caso contrário.                             #
#                                                                            #
##############################################################################

def is_prime(number: int) -> bool:
    if number in (2, 3):
        return True
    
    elif number > 3 and number % 2 != 0:
        for d in range(3, number, 2):
            if number % d == 0:
                return False
        return True
    
    else:
        return False

