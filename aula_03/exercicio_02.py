##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Exercício 02 - Classificação de Dados de Sensor ############################
#                                                                            #
# * Imagine que você está trabalhando com dados de sensores IoT. Os dados    #
#   incluem medições de temperatura. Você precisa classificar cada leitura   #
#   como 'Baixa', 'Normal' ou 'Alta'.                                        #
#                                                                            #
# * Considerando que:                                                        #
#   - Temperatura < 18 °C é 'Baixa'                                          #
#   - Temperatura >= 18 °C e <= 26°C é 'Normal'                              #
#   - Temperatura < 26 °C é 'Alta'                                           #
#                                                                            #
##############################################################################

temp = 25

if temp < 18:
    print("Temperatura Baixa.")
elif temp <= 26:
    print("Temperatura Normal.")
else:
    print("Temperatura Alta.")

