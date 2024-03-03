##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 20 ###############################################################
#                                                                            #
# * Escreva uma função que receba um dicionário e retorne uma lista de       #
#   chaves ordenadas                                                         #
#                                                                            #
##############################################################################

from typing import Any

def get_sorted_keys(dic: dict[str, Any]) -> list[str]:
    return sorted(dic.keys())


dic = {"nome": "Douglas", "idade": 30, "cidade": "Fortaleza"}
print(get_sorted_keys(dic))

