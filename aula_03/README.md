# Aula 03 - Controle de Fluxo - Debug, if, for, while, Listas e Dicionários

- Nesta aula, vamos explorar como **controlar o fluxo** de um programa utilizando as estruturas:

	- **`if`**, para tomar **decisões** baseadas em **condições**;

	- **`for`**, para **iterar** sobre **sequências** de dados; e

	- **`while`**, para **executar** um bloco de código **enquanto** uma **condição** for **verdadeira**.

- Um outro ponto importante é aprender como "**debugar**" um código, ou seja, como **analisar minuciosamente** um programa **buscando** a **fonte de um erro** que estamos enfrentando.

- Muitas IDEs, assim como o **VS Code**, contam um uma **ferramenta de debug**, que nos auxiliam a **acompanhar linha a linha** a execução de um programa, bem como **analisar** o comportamento de todas as **variáveis** existentes.

## Estruturas de Controle de Fluxo

- À medida que os **programas** ficam **mais complexos**, surge a necessidade de **controlar** o seu **fluxo de execução**.

- Por vezes, será preciso realizar **ações diferentes** com base em alguma **condição**.

- Em outros casos, é preciso **executar** uma mesma **série de comandos** **múltiplas vezes**.

- A seguir, são apresentadas as **estruturas de controle de fluxo** que nos permitem adicionar essas funcionalidades aos programas.

### Estrutura de Decisão `if`

- O **`if`** é uma **estrutura condicional** fundamental em **Python**. Com ela, é possível executar **blocos de código diferentes** de acordo com o resultado de uma **condição lógica**.

- Caso uma condição apresentada após a keyword **`if`** seja **verdadeira**, executam-se determinadas ações.

- Caso contrário, é possível **testar mais condições** usando a keyword **`elif`** (**else if**), de forma que outras ações podem ser executadas dependendo da condição que for verdadeira.

- Caso **nenhuma condição** estabelecida seja **verdadeira**, utilizamos a keyword **`else`** para determinar as ações que devem ser executadas.

#### Exemplo

```python
age = 20
if age < 18:
    print("Menor de idade.")
elif age == 18:
    print("Exatamente 18 anos.")
else:
    print("Maior de idade.")
```

### Estrutura de Repetição `for`

- A **estrutura de repetição `for`** é utilizada para **iterar** sobre os itens de qualquer **sequência**, como listas, strings, ou objetos de um dicionário, e executar um bloco de código para cada item.

- O **`for`** é especialmente útil quando precisamos executar uma **operação** para **cada elemento** de uma **coleção**.

	- Inclusive, é possível determinar **condições** sobre essas **operações** usando a estrutura **`if-elif-else`**.

- Além de iterar sobre os elementos de uma coleção, também é possível adaptar o laço **`for`** para **executar** um **bloco de código** determinado **número de vezes**, inclusive adotando um **passo definido**.

	- Para isso, usamos a **função `range()`**.

		- Para executar um bloco `n` vezes, usamos **`range(n)`**.

		- Para gerar uma sequência começando em `n0` e terminando em `n1` (não incluso), usamos **`range(n0, n1)`**. Nesse caso, o passo é unitário.

		- Para gerar uma sequência começando em `n0` e terminando em `n1` (não incluso) e com passo `s`, usamos **`range(n0, n1, s)`**.

		- Qualquer um dos parâmetros também pode ser **negativo**, de forma que é possível gerar uma lista **decrescente**.

- Também é possível **interromper** um laço **`for`** no meio de sua execução. Para tanto, usamos a keyword **`break`**.

	- Normalmente, estabelecemos uma **condição** (estrutura **`if`**) para **interrupção** do laço.

- Em vez de interromper completamente o laço, também podemos simplesmente **pular para a próxima iteração**. Para isso, temos a keyword **`continue`**.

	- Novamente, isso normalmente é feito a partir de uma **condição**.

- Para ter acesso ao **índice** referente a **cada elemento** da **coleção** dentro do bloco de código do **`for`**, podemos usar a função **`enumerate()`**, que recebe a coleção como argumento.

#### Exemplos

- Verificar o comprimento de uma lista de palavras:

	```python
	words = ["banana", "maçã", "melancia", "uva"]
	for word in words:
	    print(word, len(word))

    # Output:
    # banana 6
    # maçã 4
    # melancia 8
    # uva 3
	```

- Interrompendo o laço se a letra `x` for encontrada em uma string:

	```python
	word = "táxi"
	for letter in word:
	    print(letter)
	    if letter == "x":
	        break

    # Output:
    # t
    # á
    # x
	```

- Exibindo os múltiplos de 3 até 30:

	```python
	for i in range(3, 31, 3):
	    print(i, end=" ")

    # Output:
    # 3 6 9 12 15 18 21 24 27 30
	```

	- Note que podemos usar o parâmetro `end=" "` na função `print()` para manter as saídas na mesma linha. O padrão é `end="\n"`.

- Exibindo os índices e os elementos de uma lista:

	```python
	words = ["banana", "maçã", "melancia", "uva"]
	for i, word in enumerate(words):
	    print(i, word)

    # Output:
    # 0 banana
    # 1 maçã
    # 2 melancia
    # 3 uva
	```

### Estrutura de Repetição `while`

- A **estrutura de repetição `while`** permite executar um bloco de código repetidamente enquanto uma **condição** especificada é avaliada como verdadeira.

- Na **engenharia de dados**, o uso do loop **`while`** pode ser extremamente útil para diversas tarefas, como:

	- **Monitoramento contínuo** de **fontes de dados**.

	- **Verificação periódica** de novos **arquivos** em um **diretório**.

	- **Polling** de uma **API** para novas respostas.

	- Execução de **processos de ETL** (**Extract, Transform, Load**) até que não haja mais dados para processar.

	- Implementar **tentativas de reconexão automáticas** a **serviços** ou **bancos de dados** quando a primeira tentativa falha.

- Para implementar um **loop infinito**, utilizamos o loop **`while`** com uma **condição sempre verdadeira**, ou seja, simplesmente **`while True`**.

	> É importante usar **loops infinitos** com **cautela** para evitar criar condições em que o script possa **consumir recursos desnecessários** ou tornar-se **difícil de encerrar** de forma controlada.

- Com o uso da **biblioteca `time`**, podemos fazer com que o bloco de código do **loop `while`** seja **executado** de **forma periódica**.

	- Para isso, usamos a **função `time.sleep(t)`**, onde **`t`** é a quantidade de **segundos** que desejamos que a **execução** fique **pausada**, ou seja, é o **período de execução**.

	- Essa abordagem é **simples e eficaz** para muitos cenários de **monitoramento** e **polling** em **engenharia de dados**.

    > Em **ambientes de produção**, outras abordagens como **agendamento de tarefas** (por exemplo, usando **cron jobs** em sistemas **Unix**) ou o uso de **sistemas de enfileiramento de mensagens** e **triggers de banco de dados** podem ser **mais adequados** para algumas dessas tarefas.

- Assim como para a estrutura de repetição **`for`**, também é possível usar as **keywords `break` e `continue`** aliadas a estruturas de decisão **`if-elif-else`** em loops **`while`** para determinar a **interrupção** ou **passagem para a próxima iteração** do **bloco de código**.

#### Exemplos

- Loop infinito com execução periódica:

	```python
	# Importando a biblioteca time
	import time

	# Loop infinito
	while True:
	    print("Verificando novos dados...")
	    
	    # Aqui você pode adicionar o código para verificar novos dados,
	    # por exemplo, checar a existência de novos arquivos em um diretório,
	    # fazer uma consulta a um banco de dados ou API, etc.
	    
	    time.sleep(10)  # Pausa a execução por 10 segundos
	```

- Simulando um loop `for` com `while`:

	```python
	# Lista de palavras a ser percorrida
	words = ["banana", "maçã", "melancia", "uva"]

	# Indexador
	i = 0
	
	while i < len(words):
	    print(i, words[i])

		# Atualizando iterador
		i += 1

    # Output:
    # 0 banana
    # 1 maçã
    # 2 melancia
    # 3 uva
	```

## Exercícios

### Estrutura de Decisão `if`

- Veja os **exercícios de 01 a 05** na pasta [`exercícios`](https://github.com/kaiodt/bootcamp-data-eng/tree/main/aula_03/exercicios).

### Estrutura de Repetição `for`

- Veja os **exercícios de 06 a 10** na pasta [`exercícios`](https://github.com/kaiodt/bootcamp-data-eng/tree/main/aula_03/exercicios).

### Estrutura de Repetição `while`

- Veja os **exercícios de 11 a 15** na pasta [`exercícios`](https://github.com/kaiodt/bootcamp-data-eng/tree/main/aula_03/exercicios).

## Desafio

- Integre no [desafio](https://github.com/kaiodt/bootcamp-data-eng/blob/main/aula_02/desafio.py) da [Aula 02](https://github.com/kaiodt/bootcamp-data-eng/tree/main/aula_02) um fluxo de repetição `while` até que o usuário insira as informações corretas.

### **Solução:**

- Confira o arquivo [`desafio.py`](https://github.com/kaiodt/bootcamp-data-eng/blob/main/aula_03/desafio.py).

