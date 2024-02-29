##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 02 - TypeError, Type Check, Type Conversion, try-except e if          #
##############################################################################

# Exercício 24 - Classificador de Números #################################### 
#                                                                            #
# * Escreva um programa que solicite ao usuário para digitar um número.      #
#                                                                            #
# * Utilize `try-except` para assegurar que a entrada seja numérica e        #
#   utilize `if-elif-else` para classificar o número como "positivo",        #
#   "negativo" ou "zero".                                                    #
#                                                                            #
# * Adicionalmente, identifique se o número é "par" ou "ímpar".              #
#                                                                            #
##############################################################################

try:
    val = float(input("Digite um número: "))

    if val > 0:
        print(f"{val} é positivo.")
    elif val < 0:
        print(f"{val} é negativo.")
    else:
        print(f"{val} é igual a zero.")
    
    if val % 2 == 0:
        print(f"{val} é par.")
    else:
        print(f"{val} é ímpar.")

except ValueError as e:
    print("\nInsira um número válido.")
    print(f"[ERRO] {e}")

