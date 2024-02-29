##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Exercício 03 - Filtragem de Logs por Severidade ############################
#                                                                            #
# * Você está analisando logs de uma aplicação e precisa filtrar mensagens   #
#   com severidade `ERROR`.                                                  #
#                                                                            #
# * Dado um registro de log em formato de dicionário como mostrado a seguir, #
#   escreva um programa que imprima a mensagem se a severidade for `ERROR`.  #
#                                                                            #
#	log = {                                                                  #
#		'timestamp': '2021-06-23 10:00:00',                                  #
#		'level': 'ERROR',                                                    #
#		'message': 'Falha na conexão'                                        #
#	}                                                                        #
#                                                                            #
##############################################################################

logs = [
    {
        'timestamp': '2021-06-23 10:00:00',
        'level': 'ERROR',
        'message': 'Falha na conexão'
    },
    {
        'timestamp': '2021-06-23 11:00:00',
        'level': 'INFO',
        'message': 'Conexão estabelecida'
    },
    {
        'timestamp': '2021-06-23 11:01:00',
        'level': 'WARNING',
        'message': 'Resposta vazia'
    },
    {
        'timestamp': '2021-06-23 11:05:00',
        'level': 'ERROR',
        'message': 'Conexão perdida'
    },
]

for log in logs:
    if log['level'] == 'ERROR':
        print(log['message'])

