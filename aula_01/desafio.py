##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 01 - Variáveis em Python                                              #
##############################################################################

# Desafio ####################################################################
#                                                                            #
# * Escreva um programa em Python que solicita ao usuário para digitar seu   #
#   nome, o valor do seu salário mensal e o valor do bônus que recebeu.      #
#                                                                            #
# * O programa deve, então, imprimir uma mensagem saudando o usuário pelo    #
#   nome e informando o valor do salário em comparação com o bônus recebido. #
#                                                                            #
# * O cálculo do KPI do bônus de 2024 é de 1000 + salario * bonus            #
##############################################################################

BASE_SALLARY = 1000

name = input("Digite seu nome: ")
sallary = float(input("Digite seu salário: "))
bonus = float(input("Digite seu bonus: "))

final_bonus = BASE_SALLARY + sallary * bonus

print(f"Olá {name}, o seu bônus foi de R$ {final_bonus:.2f}.")

