##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 01 - Variáveis em Python                                              #
##############################################################################


# Comandos básicos de Python #################################################


# Função print() -------------------------------------------------------------


# Exibindo uma string
print("Hello, world!")

# Exibindo o resultado de uma operação com um inteiro e um float
print(7 + 1.3)

# Exibindo uma lista:
print([1, 2, 'a', 'b'])

# Exibindo múltiplos argumentos
print("Hello", 13, 3.14)

print()

# Função input() -------------------------------------------------------------


# Solicitando a entrada do usuário
input("Digite seu nome: ")
print()

# Usando a entrada do usuário em uma operação
print("Olá, " + input("Digite seu nome: ") + "!")
print()

# Convertendo a entrada do usuário em um valor inteiro:
print(int(input("Digite um inteiro: ")) + float(input("Digite um float: ")))
print()

# Variáveis ------------------------------------------------------------------


# Criando variáveis de vários tipos

a = True                # Booleano
b = 13                  # Inteiro
c = 3.14                # Float
d = "Hello"             # String
e = [1, 2, 3]           # Lista
f = (1, 2, 3)           # Tupla
g = {"a": 1, "b": 2}    # Dicionário

# Atribuindo uma entrada de usuário a uma variável
name = input("Digite seu nome: ")
print(f"Olá, {name}!")
print()

# Mudando o tipo de dado de uma variável
a = 100
print(type(a))

a = "Hello"
print(type(a))

