##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 15 - Contagem de Frequência de Itens #############################
#                                                                            #
# * Dada uma string, contar a frequência de cada caractere usando um         #
#   dicionário.                                                              #
#                                                                            #
##############################################################################

string = "Engenharia de Dados"

char_counts = {}
for char in string.lower():
    # Contar apenas caracteres diferentes de espaço
    if char != " ":
        char_counts[char] = char_counts.get(char, 0) + 1

print(char_counts)

