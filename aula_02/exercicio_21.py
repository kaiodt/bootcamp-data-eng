##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 02 - TypeError, Type Check, Type Conversion, try-except e if          #
##############################################################################

# Exercício 21 - Conversor de Tempeartura ####################################
#                                                                            #
# * Escreva um programa que converta a temperatura de Celsius para           #
#   Fahrenheit.                                                              #
#                                                                            #
# * O programa deve solicitar ao usuário a temperatura em Celsius e,         #
#   utilizando `try-except`, garantir que a entrada seja numérica, tratando  #
#   qualquer `ValueError`.                                                   #
#                                                                            #
# * Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada   #
#   não for válida.                                                          #
#                                                                            #
##############################################################################

try:
    temp_C = float(input("Digite a temperatura em Celcius: "))
    temp_F = 32 + (temp_C * 9/5)

    print(f"{temp_C} °C = {temp_F:.2f} °F")

except ValueError as e:
    print("Forneça um valor numérico válido.")
    print(f"[ERRO] {e}")

