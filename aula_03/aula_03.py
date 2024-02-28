##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################


# Estrutura de Decisão if ####################################################


age = 20

if age < 18:
    print("Menor de idade.")
elif age == 18:
    print("Exatamente 18 anos.")
else:
    print("Maior de idade.")

print()


# Estrutura de Repetição for #################################################


# Verificar o comprimento de uma lista de palavras ---------------------------


words = ["banana", "maçã", "melancia", "uva"]

for word in words:
    print(word, len(word))

print()


# Interrompendo o laço se a letra `x` for encontrada em uma string -----------


word = "táxi"

for letter in word:
    print(letter)
    if letter == "x":
        break

print()


# Exibindo os múltiplos de 3 até 30 ------------------------------------------


for i in range(3, 31, 3):
    print(i, end=" ")

print("\n")


# Exibindo os índices e os elementos de uma lista ----------------------------


words = ["banana", "maçã", "melancia", "uva"]

for i, word in enumerate(words):
    print(i, word)

print()


# Estrutura de Repetição while ###############################################


# Loop infinito com execução periódica ---------------------------------------


# Importando a biblioteca time
import time

# Contador de execuções
count = 3

# Loop infinito
while True:
    print("Verificando novos dados...")
    
    # Aqui você pode adicionar o código para verificar novos dados,
    # por exemplo, checar a existência de novos arquivos em um diretório,
    # fazer uma consulta a um banco de dados ou API, etc.
    
    time.sleep(10)  # Pausa a execução por 10 segundos

    # Atualizar contador
    count -= 1

    # Interromper se o contador estiver zerado
    if count == 0:
        break

print()


# Simulando um loop for com while --------------------------------------------


# Lista de palavras a ser percorrida
words = ["banana", "maçã", "melancia", "uva"]

# Indexador
i = 0

while i < len(words):
    print(i, words[i])

    # Atualizando iterador
    i += 1

