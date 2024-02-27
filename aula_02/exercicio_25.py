##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 02 - TypeError, Type Check, Type Conversion, try-except e if          #
##############################################################################

# Exercício 25 - Conversão de Tipo com Validação ############################# 
#                                                                            #
# * Crie um script que solicite ao usuário uma lista de números separados    #
#   por vírgula. O programa deve converter a string de entrada em uma        #
#   lista de números inteiros.                                               #
#                                                                            #
# * Utilize `try-except` para tratar a conversão de cada número e validar    #
#   que cada elemento da lista convertida é um inteiro.                      #
#                                                                            #
# * Se a conversão falhar ou um elemento não for um inteiro, imprima uma     #
#   mensagem de erro. Se a conversão for bem-sucedida para todos os          #
#   elementos, imprima a lista de inteiros.                                  #
#                                                                            #
##############################################################################

try:
    numbers_in = input("Digite números inteiros separados por vírgula: ")

    numbers = [int(number) for number in numbers_in.split(",")]
    print(f"Lista de números: {numbers}")

except ValueError as e:
    print("\nInsira apenas números inteiros válidos.")
    print(f"[ERRO] {e}")

