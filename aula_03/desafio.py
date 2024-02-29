##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Desafio ####################################################################
#                                                                            #
# * Integre na solução da Aula 02 um fluxo de repetição `while` até que o    #
#   usuário insira as informações corretas.                                  #
#                                                                            #
##############################################################################

BASE_SALLARY = 1000

# Obter o nome do usuário
while True:
    try:
        # Solicitar nome do usuário
        name = input("Digite seu nome: ")

        # Não aceitar um nome vazio
        if len(name) == 0:
            raise ValueError("Você não digitou o seu nome.")
        
        # Não aceitar apenas espaços no nome
        elif name.isspace():
            raise ValueError("Você digitou apenas espaços no seu nome.")

        # Aceitar apenas letras (espaços entre os nomes são permitidos)
        elif not name.replace(" ", "").isalpha():
            raise ValueError("Use apenas letras no seu nome.")
        
        else:
            break

    except ValueError as e:
        print(f"\n[ERRO] {e}")
        print("Tente novamente.\n")

print()

# Obter o salário do usuário
while True:
    try:
        # Solicitar salário
        sallary = float(input("Digite seu salário: "))

        # Não aceitar salário negativo
        if sallary < 0:
            raise ValueError("Insira um salário positivo.", True)
        else:
            break

    except ValueError as e:
        if len(e.args) > 1:
            print(f"\n[ERRO] {e.args[0]}")
        else:
            print("\n[ERRO] O valor inserido é inválido.")
        
        print("Tente novamente.\n")

print()

# Obter o bônus do usuário
while True:
    try:
        # Solicitar bônus
        bonus = float(input("Digite seu bonus: "))

        # Não aceitar bônus menor que 1
        if bonus < 1:
            raise ValueError("Insira um bônus maior ou igual a um.", True)
        else:
            break

    except ValueError as e:
        if len(e.args) > 1:
            print(f"\n[ERRO] {e.args[0]}")
        else:
            print("\n[ERRO] O valor inserido é inválido.")
        
        print("Tente novamente.\n")

print()

# Cálculo do bônus final
final_bonus = BASE_SALLARY + sallary * bonus

print(f"Olá {name}, o seu bônus foi de R$ {final_bonus:.2f}.")

