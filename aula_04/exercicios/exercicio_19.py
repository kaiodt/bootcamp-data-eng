##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 19 ###############################################################
#                                                                            #
# * Implemente uma função que receba dois argumentos: uma lista de números e #
#   um número. A função deve retornar todas as combinações de pares na lista #
#   que somem ao número dado.                                                #
#                                                                            #
##############################################################################

def get_combinations(numbers: list[float], comb_sum: float) -> \
    list[tuple[float, float]]:

    number_combs = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == comb_sum:
                number_combs.append((numbers[i], numbers[j]))

    return number_combs

print(get_combinations([1, 2, 3, 4, 2], 5))


# Solução Alternativa  #######################################################


from itertools import combinations

def get_combinations(numbers: list[float], comb_sum: float) -> \
    list[tuple[float, float]]:

    return [(a, b) for a, b in combinations(numbers, 2) if a + b == comb_sum]

print(get_combinations([1, 2, 3, 4, 2], 5))

