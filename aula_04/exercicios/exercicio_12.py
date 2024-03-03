##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 12 - Fusão de Dicionários ########################################
#                                                                            #
# * Dados dois dicionários, fundi-los em um único dicionário.                #
#                                                                            #
##############################################################################

dict_1 = {"a": 1, "b": 2}
dict_2 = {"c": 3, "d": 4}

full_dict = {**dict_1, **dict_2}

print(full_dict)

