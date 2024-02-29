##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 02 - TypeError, Type Check, Type Conversion, try-except e if          #
##############################################################################

# Exercício 23 - Calculadora Simples #########################################
#                                                                            #
# * Desenvolva uma calculadora simples que aceite duas entradas numéricas e  #
#   um operador (+, -, *, /) do usuário.                                     #
#                                                                            #
# * Use `try-except` para lidar com divisões por zero e entradas não         #
#   numéricas.                                                               #
#                                                                            #
# * Utilize `if-elif-else` para realizar a operação matemática baseada no    #
#   operador fornecido.                                                      #
#                                                                            #
# * Imprima o resultado ou uma mensagem de erro apropriada.                  #
#                                                                            #
##############################################################################

try:
    val_1 = float(input("Digite o primeiro valor: "))
    op = input("Digite o operador: ")
    val_2 = float(input("Digite o segundo valor: "))

    if op == "+":
        res = val_1 + val_2
    elif op == "-":
        res = val_1 - val_2
    elif op == "*":
        res = val_1 * val_2
    elif op == "/":
        res = val_1 / val_2
    else:
        res = None
    
    if res is not None:
        print(f"\n{val_1} {op} {val_2} = {res}\n")
    else:
        print(f"\n{op} não é um operador inválido.")

except ValueError as e:
    print("\nInsira um número válido.")
    print(f"[ERRO] {e}")

except ZeroDivisionError as e:
    print("\nDivisão por zero não permitida.")
    print(f"[ERRO] {e}")

