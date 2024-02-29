##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Exercício 04 - Validação de Dados de Entrada ###############################
#                                                                            #
# * Antes de processar os dados de usuários em um sistema de recomendação,   #
#   você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e  #
#   tenha fornecido um email válido.                                         #
#                                                                            #
# * Escreva um programa que valide essas condições e imprima "Dados de       #
#   usuário válidos" ou o erro específico encontrado.                        #
#                                                                            #
##############################################################################

user_age = 30
user_email = "user@email.com"

if (user_age < 18) or (user_age > 65):
    print("A idade deve ser de 18 a 65 anos.")
elif ("@" not in user_email) or ("." not in user_email):
    print("Email inválido.")
else:
    print("Dados de usuário válidos.")

