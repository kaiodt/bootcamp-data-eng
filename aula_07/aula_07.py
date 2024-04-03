##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 07 - Funções em Python e Estruturas de Dados - Parte 1                #
##############################################################################


# Definindo Funções ##########################################################

def my_function():
    return "Hello, World!"

# Parâmetros e Argumentos ####################################################

def my_sum(a, b):
    return a + b

# Chamando Funções ###########################################################

print(f"my_function() -> {my_function()}")

print()

result = my_sum(5, 3)
print(f"my_sum(5, 3) -> {result}")

print()

# Valores Padrão e Argumentos Nomeados #######################################

def greeting(name, message="Olá"):
    print(f"{message}, {name}!")

print("greeting('Kaio')")
greeting("Kaio")

print()

print("greeting(message='Bem-vindo', name='Kaio')")
greeting(message="Bem-vindo", name="Kaio")

