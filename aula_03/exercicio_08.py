##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Exercício 08 - Filtragem de Dados Faltantes ################################
#                                                                            #
# * Dada uma lista de dicionários representando dados de usuários, filtrar   #
#   aqueles que têm um campo específico faltando.                            #
#                                                                            #
##############################################################################

users = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"},
    {"nome": "", "email": "drew@example.com"},
]

valid_users = []
for user in users:
    # Testar se os valores de todos os campos estão preenchidos
    valid = True
    for value in user.values():
        # Caso um valor não estiver preenchido, usuário inválido
        if not value:
            valid = False
            break
    
    # Guardar apenas usuários válidos
    if valid:
        valid_users.append(user)

print(valid_users)


# Versão alternativa #########################################################


users = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"},
    {"nome": "", "email": "drew@example.com"},
]

valid_users = [user for user in users if all(user.values())]

print(valid_users)

