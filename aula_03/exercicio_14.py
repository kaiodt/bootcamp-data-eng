##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Exercício 14 - Tentativas de Conexão #######################################
#                                                                            #
# * Simular tentativas de reconexão a um serviço com um limite máximo de     #
#   tentativas.                                                              #
#                                                                            #
##############################################################################

MAX_TRIALS = 3
trial = 1

while trial <= MAX_TRIALS:
    print(f"Tentativa de conexão {trial}/{MAX_TRIALS}.")

    # Código para tentativa de conexão
    connected = False

    if connected:
        print("\nConexão bem-sucedida!")
        break
    else:
        trial += 1

else:
    print(f"\nNão foi possível conectar após {MAX_TRIALS} tentativas.")

