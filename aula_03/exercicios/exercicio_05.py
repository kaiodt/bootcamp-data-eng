##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Exercício 05 - Detecção de Anomalias em Dados de Transações ################
#                                                                            #
# * Você está trabalhando em um sistema de detecção de fraude e precisa      #
#   identificar transações suspeitas.                                        #
#                                                                            #
# * Uma transação é considerada suspeita se o valor for superior a           #
#   R$ 10.000,00 ou se ocorrer fora do horário comercial (antes das 9h ou    #
#   depois das 18h).                                                         #
#                                                                            #
# * Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`,      #
#   verifique se ela é suspeita.                                             #
#                                                                            #
##############################################################################

MAX_AMOUNT = 10000
COM_HOUR_BEG = 9
COM_HOUR_END = 18

transaction = {
    "amount": 8500,
    "hour": 17
}

if transaction["amount"] > MAX_AMOUNT:
    print("Transação suspeita: Valor acima do máximo.")
elif (transaction["hour"] < COM_HOUR_BEG) or \
        (transaction["hour"] > COM_HOUR_END):
    print("Transação suspeita: Fora do horário comercial.")
else:
    print("Transação válida.")

