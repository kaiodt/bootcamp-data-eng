# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs. Tabelas vs. Excel) e Funções

- Nesta aula vamos aprender sobre:

	- Type Hint

	- Listas

	- Dicionários

	- Funções

- Esses elementos são essenciais para a **manipulação de dados**, ajudando na **organização**, **interpretação** e **análise** eficiente das informações.

## Type Hint

- **Type Hint**, como o nome sugere, significa introduzir **indicações** sobre os **tipos de dados** em definições de **variáveis**, **parâmetros e retorno de funções e métodos** e **atributos de classes**.

- O uso de **Type Hint** torna o **código mais legível e seguro**, especificando o **tipo de dados esperados** em vários pontos, como nas chamadas de funções e métodos.

- Embora essa indicação possa ser feita por meio de **comentários**, o uso de **Type Hint** é **mais indicado**, já que é pensado especificamente para este fim.

- O **Type Hint** foi introduzido a partir do **Python 3.5**,  através da **PEP 484**.

- Na **engenharia de dados**, o **Type Hint** é especialmente útil para **garantir** que as **funções de manipulação** e **análise de dados** recebam os **dados no formato correto**, **reduzindo erros** em tempo de execução.

> É importante ressaltar que o **Type Hint** é realmente **apenas uma indicação** dos **tipos de dados**, **não** sendo estritamente **aplicadas** em **tempo de execução**. A **verificação** sobre a observância desses tipos **ainda precisa ser feita**!

### Exemplo

- Podemos usar Type Hint na definição de variáveis, indicando qual o seu tipo.

	```python
	age: int = 30
	height: float = 1.75
	name: str = "Alice"
	is_student: bool = True
	```

### Tipagem Forte vs. Fraca

- **Tipagem Forte:**

	- Em linguagens com **tipagem forte**, os objetos possuem **tipos bem definidos** e esses tipos **definem o comportamento** dos objetos nas **operações**. Portanto, operações que envolvem **tipos incompatíveis** (por exemplo, somar um inteiro com uma string) resultarão em **erro**. **Python** é uma linguagem com **tipagem forte**.

- **Tipagem Fraca:**

	- Linguagens com **tipagem fraca** permitem maior **flexibilidade** nas **operações** entre **diferentes tipos**, fazendo **conversões** de tipo **implícitas**. **JavaScript** é um exemplo clássico de linguagem com **tipagem fraca**, onde é possível, por exemplo, adicionar números a strings sem erros.

### Tipagem Dinâmica vs. Estática

- **Tipagem Dinâmica:**

	- Em linguagens com **tipagem dinâmica**, como em **Python**, os **tipos dos dados** são **inferidos** em **tempo de execução**, **não** precisando ser **declarados explicitamente**, pois isso é feito de forma **automática**. Além disso, o **tipo de dado** de uma **variável** pode **mudar** durante a **execução**. Isso oferece **flexibilidade** e **rapidez** no desenvolvimento, mas pode aumentar o **risco de erros de tipo** que só serão detectados em tempo de execução.

- **Tipagem Estática:**

	- Linguagens com **tipagem estática**, como **Java** e **C++**, exigem que o **tipo** de cada **variável** seja **declarado explicitamente** no momento da **compilação**. Isso ajuda a **detectar erros** de tipo **antes da execução** do programa, aumentando a **segurança de tipos** e potencialmente **melhorando** o **desempenho**.

## Tipos Complexos - Listas e Dicionários

- **Listas** e **dicionários** são estruturas de dados **versáteis** que permitem **armazenar** e **manipular** **coleções de dados** de forma eficiente.

- As **listas** podem armazenar **qualquer tipo de dados** existentes em **Python**, inclusive **outras listas** e **classes definidas** pelo usuário. Os elementos são dispostos de forma **ordenada** e são **mutáveis**.

- Os **dicionários** armazenam pares **chave-valor**, por exemplo, `{"nome": "Kaio", "idade": 30}`. A partir do **Python 3.7**, os pares chave-valor em um dicionário passaram a ser **ordenados**. Os valores também são **mutáveis**.

- Na **engenharia de dados**, essas estruturas são fundamentais para **organizar dados coletados de diversas fontes**, facilitando operações como **filtragem**, **busca**, **agregação** e **transformação de dados**.

### Exercícios

- Veja os **exercícios de 01 a 15** na pasta [`exercícios`](https://github.com/kaiodt/bootcamp-data-eng/tree/main/aula_04/exercicios).

## Leitura de Arquivos `csv`

- O **Python** conta com um **módulo nativo de `csv`**, que nos permite **ler** e **manipular** arquivos com essa extensão.

- Quando manipulamos arquivos, é importante usar a **estrutura de gerenciamento de contexto `with`**:

	```python
	with open("<path>") as file:
		# Manipulação do arquivo a partir do handle `file`
	```

	- Com isso, garantimos que, **após realizar todas as operações** com o arquivo que foi aberto, ou quando **erros** ocorrem, o **arquivo será fechado**, para que não ocupe **espaço desnecessário na memória**.

### Exemplo

```python
import csv

# Caminho para o arquivo csv
path = "exemplo.csv"

# Lista vazia para armazenar os dados
data = []

# Usando o gerenciador de contexto `with` para manipular o arquivo
with open(path, mode="r", encoding="utf-8") as file:
    # Objeto leitor de csv em forma de dicionário
    dict_reader = csv.DictReader(file)

    # Lendo cada linha do arquivo csv
    for row in dict_reader:
        # Adicionando linha (dicionário) à lista de dados
        data.append(row)

# Exibindo os dados lidos
for row in data:
    print(row)
```

## Funções

- As **funções** são um dos principais componentes da programação. Permitem **encapsular blocos de código** responsáveis por realizar **tarefas específicas**.

- Uma **função** pode receber valores em sua **entrada**, que são **processados** para gerar uma **saída**.

- Com o uso de funções, é possível **modularizar** e **reaproveitar** partes de um programa, tornando o seu **código mais organizado e legível**, bem como facilita a **manutenção**.

- Além disso, as funções proporcionam uma **abstração de detalhes** sobre como uma operação é realizada, independente da complexidade envolvida. Com isso, pode-se pensar em um **nível mais alto**.

- Na **engenharia de dados**, funções são usadas para encapsular **lógicas de transformação**, **limpeza**, **agregação** e **análise de dados**, tornando o **código** mais **organizado** e com **qualidade**.

### Exemplos

- Desenvolvendo uma função em Python que ordena uma lista usando o **algoritmo de ordenação por seleção**, um método simples, mas eficaz, para **listas pequenas e médias**.

    ```python
    def sort_list(list_in: list) -> list:
        """
        Ordena uma lista usando o algoritmo de ordenação por seleção.
        """
        # Fazendo uma cópia da lista de entrada
        sorted_list = list_in.copy()
    
        for i in range(len(sorted_list) - 1):
            # Loop dos elementos após o índice i
            for j in range(i+1, len(sorted_list)):
                # Se o elemento do índice i for maior que algum elemento
                # depois dele, suas posições são trocadas.
                if sorted_list[i] > sorted_list[j]:
                    sorted_list[i], sorted_list[j] = \
                        sorted_list[j], sorted_list[i]
        return sorted_list
    
    # Lista a ser ordenada
    list_to_sort = [64, 34, 25, 12, 22, 11, 90]
    
    # Usando a função
    sorted_list = sort_list(list_to_sort)
    print(sorted_list)
    ```

- Apesar da possibilidade de criação de funções para a solução de problemas específicos, sempre é importante **buscar se já não há uma solução** disponibilizada pelo próprio **Python**, ou em alguma **biblioteca de terceiros**.

	- Muito provavelmente, a **solução já existente** é **otimizada** e já foi **amplamente testada**. Portanto, é **mais rápido** e **seguro** utilizá-las.

- Por exemplo, em vez de escrever uma função para ordenação como acima, poderíamos utilizar a **função built-in `sorted`** do Python, ou o **método `.sort`** disponível para listas.

	```python
	# Lista a ser ordenada
	list_to_sort = [64, 34, 25, 12, 22, 11, 90]

	# Ordenar usando a função sorted
	sorted_list = sorted(list_to_sort)

	# Ordenar usando o método .sort
	# Uma cópia da lista original é feita, pois o método .sort faz a
	# ordenação in-place
	sorted_list = list_to_sort.copy()
	sorted_list.sort()
	```

- Em outros **casos mais específicos**, o uso de **funções dedicadas** é mais **adequado**. Por exemplo, suponha que é preciso limpar e transformar nomes de usuários em um conjunto de dados.

    ```python
    def normalize_name(name: str) -> str:
        """
        Normaliza nomes de usuário: Remove espaços no início e fim e
        transforma em minúsculas.
        """
        return name.strip().lower()

    # Usando a função
    names = [" Alice ", "BOB", "Carlos"]
    normalized_names = [normalize_name(name) for name in names]
    print(normalized_names)
    ```

### Padrão de Nomeação de Funções

- O **padrão de nomeação de funções** em **Python** segue **convenções** que são recomendadas na **PEP 8**, o **guia de estilo** para a **codificação em Python**.

- Adotar esses padrões não só **melhora a legibilidade** do código, como também **facilita a compreensão** e a **manutenção** por outros desenvolvedores, ou por você mesmo no futuro.

- **Nomes claros e descritivos:**

	- O nome de uma função deve ser **descritivo** o suficiente para **indicar sua finalidade** ou o que ela faz.
	- Por exemplo, `calcular_area_circulo` é mais descritivo do que simplesmente `area`.

- **Letras minúsculas separadas por underscores (`snake_case`):**

	- Funções em Python devem ser nomeadas usando **letras minúsculas**, com **palavras separadas** por **underscores** (**`_`**) para melhorar a **legibilidade**.

	- Este estilo é algumas vezes referido como **`snake_case`**.

	- Por exemplo, `carregar_dados_usuario` é um nome adequado para uma função.

- **Evitar nomes genéricos:**

	- Nomes como `processo`, `executar`, ou `fazer_algo` são muito **genéricos** e **não fornecem informações suficientes** sobre o que a função faz.

	- Prefira nomes que ofereçam um **nível adequado de detalhe**.

- **Evitar abreviações obscuras:**

	- Embora **abreviações** possam **encurtar o nome** de uma função, elas podem tornar o código **menos acessível** para outros desenvolvedores.

	- Por exemplo, `calc_media_notas` é preferível a `cmn`.

- **Prefixos com verbos:**

	- Muitas vezes, funções realizam **ações**, então é útil **iniciar o nome** da função com um **verbo que descreve** essa **ação**, como `obter_`, `calcular_`, `processar_`, `validar_` ou `limpar_`.

### Type Hint para Parâmetros

- Como mencionado anteriormente, também podemos utilizar **Type Hint** para **indicar** os **tipos de dados** esperados para cada **parâmetro** da **função**, bem como o tipo de dados do que ela **retorna**.

- Por isso, **Type Hint** é uma prática extremamente útil para **análise estática de código**, melhorando sua **legibilidade** e ajudando na **detecção precoce de erros**.

> Lembre-se que essas indicações de tipo **não são estritamente aplicadas** em **tempo de execução**. Portanto, **devem ser verificadas** caso necessário.

#### Exemplo

```python
def greeting(name: str, age: int) -> str:
	return f"Olá, {name}, você tem {age} anos."
```

### Valores Default de Parâmetros

- Em Python, é possível **definir valores default** para os **parâmetros** de uma **função**, tal que a função pode ser chamada sem fornecer todos os argumentos, desde que os omitidos tenham um valor padrão definido.

- A **tipagem** funciona da mesma forma, com o tipo sendo especificado antes do sinal de igual.

#### Exemplo

```python
def greeting(name: str, age: int = 30) -> str:
	return f"Olá, {name}, você tem {age} anos."
```

### Exercícios

- Veja os **exercícios de 15 a 20** na pasta [`exercícios`](https://github.com/kaiodt/bootcamp-data-eng/tree/main/aula_04/exercicios).

## Desafio

- Refatorar o código do [desafio](https://github.com/kaiodt/bootcamp-data-eng/blob/main/aula_03/desafio.py) desenvolvido na [Aula 03](https://github.com/kaiodt/bootcamp-data-eng/tree/main/aula_03) usando dicionário, funções e tipagem.

### **Solução:**

- Confira o arquivo [`desafio.py`](https://github.com/kaiodt/bootcamp-data-eng/blob/main/aula_04/desafio.py).

