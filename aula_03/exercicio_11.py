##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Exercício 11 - Leitura de Dados até Flag ###################################
#                                                                            #
# * Ler dados de entrada até que uma palavra-chave específica ("sair") seja  #
#   fornecida.                                                               #
#                                                                            #
##############################################################################

data = []

while True:
    in_value = input("Digite um valor (ou 'sair' para terminar): ")

    if in_value.lower() == "sair":
        break
    else:
        data.append(in_value)

print()
print(data)

