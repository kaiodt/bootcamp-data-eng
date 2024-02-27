##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 02 - TypeError, Type Check, Type Conversion, try-except e if          #
##############################################################################

# Exercício 22 - Verificador de Palíndromo ###################################
#                                                                            #
# * Crie um programa que verifica se uma palavra ou frase é um palíndromo    #
#   (lê-se igualmente de trás para frente, desconsiderando espaços e         #
#   pontuações).                                                             #
#                                                                            #
# * Utilize algum método para garantir que a entrada seja uma string.        #
#                                                                            #
# * Dica: Utilize a função `isinstance()` para verificar o tipo da entrada.  #
#                                                                            #
##############################################################################

phrase = input("Digite uma palavra ou frase: ")

if isinstance(phrase, str):
    formatted_phrase = phrase.replace(" ", "").lower()

    if formatted_phrase == formatted_phrase[::-1]:
        print(f"'{phrase}' é um palíndromo.")
    else:
        print(f"'{phrase}' não é um palíndromo.")

else:
    print("Insira uma palavra ou frase válida.")

