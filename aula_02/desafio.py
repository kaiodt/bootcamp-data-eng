##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 02 - TypeError, Type Check, Type Conversion, try-except e if          #
##############################################################################

# Desafio ####################################################################
#                                                                            #
# * Refatore o desafio da Aula 01 evitando bugs onde é possível que possam   #
#   acontecer.                                                               #
#                                                                            #
# * Para tratar entradas inválidas que não podem ser convertidas para um     #
#   número de ponto flutuante e prevenção de valores negativos para salário  #
#   e bônus, você pode modificar o código diretamente.                       #
#                                                                            #
# * Isso envolve adicionar verificações adicionais após a tentativa de       #
#   conversão para garantir que os valores sejam positivos.                  #
#                                                                            #
# * O cálculo do KPI do bônus de 2024 é de 1000 + salario * bonus            #
#                                                                            #
##############################################################################

BASE_SALLARY = 1000

try:
    # Solicitar nome do usuário
    name = input("Digite seu nome: ")

    # Não aceitar um nome vazio
    assert len(name) > 0, "Você não digitou o seu nome."

    # Não aceitar apenas espaços no nome
    assert not name.isspace(), "Você digitou apenas espaços no seu nome."

    # Aceitar apenas letras no nome (espaços entre os nomes são permitidos)
    assert name.replace(" ", "").isalpha(), \
        "Certifique-se de usar apenas letras no seu nome."

    # Solicitar salário
    sallary = float(input("Digite seu salário: "))

    # Não aceitar salário negativo
    assert sallary >= 0, "Insira um salário positivo."

    # Solicitar bônus
    bonus = float(input("Digite seu bonus: "))

    # Não aceitar bônus menor que 1
    assert bonus >= 1, "Insira um bônus maior ou igual a um."

    # Cálculo do bônus final
    final_bonus = BASE_SALLARY + sallary * bonus

    print(f"\nOlá {name}, o seu bônus foi de R$ {final_bonus:.2f}.")

except AssertionError as msg:
    print(f"\n[ERRO] {msg}")

except ValueError as e:
    print("[ERRO] O valor inserido é inválido.")
    print(f"[ERRO] {e}.")

