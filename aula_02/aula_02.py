##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 02 - TypeError, Type Check, Type Conversion, try-except e if          #
##############################################################################


# TypeError ##################################################################


# Exemplo de TypeError -------------------------------------------------------


# print(len(7))
# Output: TypeError: object of type 'int' has no len()


# Type Check #################################################################


# Função type() --------------------------------------------------------------


print(type(7))
print(type(3.14))
print(type("Hello"))
print(type(True))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({"a": 1, "b": 2}))
print()


# Função isinstance() --------------------------------------------------------


print(isinstance(7, int))
print(isinstance(3.14, int))
print(isinstance("Hello", str))
print(isinstance("True", bool))
print(isinstance([1, 2, 3], list))
print(isinstance((1, 2, 3), tuple))
print(isinstance({"a": 1, "b": 2}, dict))
print()


# Type Conversion ############################################################


# Convertendo um número em formato string para float e realizando
# uma operação
print(float("3.14") + 4.25)
print()

# Tratamento de Erros com try-except #########################################


# Divisão por zero -----------------------------------------------------------


try:
    # Trecho de código que pode gerar uma exceção
    result = 10 / 0
    
except ZeroDivisionError:
    # Código executado se a exceção ocorrer
    print("Divisão por zero não é permitida.")
    
else:
    # Código executado somente se são houve exceção
    print("Código executado com sucesso!")
    
finally:
    # Código executado independente da ocorrência de exceções
    print("Sempre executado.")

print()


# Exceção genérica -----------------------------------------------------------


try:
    # Trecho de código que pode gerar uma exceção
    length = len(10)

except Exception as e:
    # Apresentando o tipo de erro
    print(type(e))
    
    # Apresentando a mensagem de erro
    print(e)
    
else:
    # Código executado somente se são houve exceção
    print("Código executado com sucesso!")
    
finally:
    # Código executado independente da ocorrência de exceções
    print("Sempre executado.")

print()

