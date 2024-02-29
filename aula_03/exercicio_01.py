##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Exercício 01 - Verificador de Palíndromo ###################################
#                                                                            #
# * Você está analisando um conjunto de dados de vendas e precisa garantir   #
#   que todos os registros tenham valores positivos para `quantidade` e      #
#   `preço`.                                                                 #
#                                                                            #
# * Escreva um programa que verifique esses campos e imprima "Dados válidos" #
#   se ambos forem positivos ou "Dados inválidos" caso contrário.            #
#                                                                            #
##############################################################################

quantidade = -10
preco = 20

if quantidade > 0 and preco > 0:
    print("Dados válidos.")
else:
    print("Dados inválidos.")

