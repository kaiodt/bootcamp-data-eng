##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Exercício 15 - Processamento de Dados com Condição de Parada ###############
#                                                                            #
# * Processar itens de uma lista até encontrar um valor específico que       #
#   indica a parada.                                                         #
#                                                                            #
##############################################################################

# Lista a processar
items = [1, 2, 3, "x", 4, 5]

# Itens processados
proc_items = []

i = 0
while i < len(items):
    print(f"Processando item {items[i]}...")

    if items[i] != "x":
        print("Item processado.\n")
        proc_items.append(items[i])
        i += 1
    else:
        print("Interrompendo processamento...\n")
        break

print(f"Itens processados: {proc_items}")

