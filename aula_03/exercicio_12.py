##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Exercício 12 - Validação de Entrada ########################################
#                                                                            #
# * Solicitar ao usuário um número dentro de um intervalo específico até que #
#   a entrada seja válida.                                                   #
#                                                                            #
##############################################################################

INT_MIN = 0
INT_MAX = 10

while True:
    try:
        value = int(input(f"Digite um número entre {INT_MIN} e {INT_MAX}: "))

        if INT_MIN <= value <= INT_MAX:
            break
        else:
            print(f"\nO valor inserido não está entre {INT_MIN} e {INT_MAX}.\n")

    except ValueError:
        print("\nValor inserido inválido.\n")


print(f"\nO número {value} está entre {INT_MIN} e {INT_MAX}.")

