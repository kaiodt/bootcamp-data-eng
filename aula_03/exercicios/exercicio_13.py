##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Exercício 13 - Consumo de API Simulado #####################################
#                                                                            #
# * Simular o consumo de uma API paginada, onde cada "página" de dados é     #
#   processada em loop até que não haja mais páginas.                        #
#                                                                            #
##############################################################################

current_page = 1
total_pages = 5  # Simulação, na prática, isso viria da API

while current_page <= total_pages:
    print(f"Processando página {current_page}/{total_pages}...")
    current_page += 1

print("Todas as páginas foram processadas.")

