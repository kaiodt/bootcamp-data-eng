##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Exercício 02 ###############################################################
#                                                                            #
# * Dada a lista `["Python", "Java", "C++", "JavaScript"]`, remova o item    #
#   "C++" e adicione "Ruby".                                                 #
#                                                                            #
##############################################################################

languages = ["Python", "Java", "C++", "JavaScript"]

# Removendo C++
languages.remove("C++")

# Adicionando "Ruby"
languages.append("Ruby")

print(languages)

