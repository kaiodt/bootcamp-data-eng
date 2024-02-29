##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários  #
##############################################################################

# Exercício 06 - Contagem de Palavras em Textos ##############################
#                                                                            #
# * Dado um texto, contar quantas vezes cada palavra única aparece nele.     #
#                                                                            #
##############################################################################

# Importando a bilbioteca de regex
import re

# Texto a ser analisado
text = '''
Então ele disse:
"Veja, você acha que 2 é o número certo?"
Eu disse:
"Ele acha que é certo, sim!"
'''

# Substituindo quebras de linha (\n) por espaços
text = text.replace("\n", " ")

# Removendo números e pontuações do texto usando regex

# A função re.sub() substitui qualquer match do padrão por uma string
# desejada, nesse caso uma string vazia.

# O primeiro grupo, [^\w\s], excluirá qualquer coisa que NÃO seja uma letra,
# número, ou espaço.

# O segundo grupo, [\d], excluirá qualquer número.

# O parâmetro `flags=re.UNICODE` faz com que caracteres especiais sejam
# considerados como letras.

clean_text = re.sub(r'[^\w\s]|[\d]', '', text, flags=re.UNICODE)

# Removendo espaços no início e fim e transformando em minúsculas
clean_text = clean_text.strip().lower()

# Contando as palavras do texto
word_counts = {}
for word in clean_text.split(" "):
    # Considerar apenas palavras válidas
    if len(word) > 0:
        # Incremetar contagem da palavra se ela já existir no dicionário,
        # ou adicioná-la com contagem 1, caso contrário.
        word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)

