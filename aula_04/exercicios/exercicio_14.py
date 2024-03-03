##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 14 - Extração de Chaves e Valores ################################
#                                                                            #
# * Dado um dicionário, criar listas separadas para suas chaves e valores.   #
#                                                                            #
##############################################################################

dic = {"a": 1, "b": 2, "c": 3}

dic_keys = list(dic.keys())
dic_values = list(dic.values())

print(f"Chaves: {dic_keys}")
print(f"Valores: {dic_values}")

