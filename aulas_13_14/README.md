# Aulas 13 e 14 - Herança e Polimorfismo

- Nesta aula, continuaremos o estudo da **Programação Orientada a Objetos** (**POO**) em **Python** por meio da solução de um desafio.


## Desafio

- Sua empresa recebe arquivos nos formatos `.csv` e `.txt` em duas pastas distintas, de forma contínua.

- Você precisa consolidá-los em um único dataframe.

- Qual seria a melhor abordagem para realizar essa tarefa?


## Classes Abstratas, Herança e Polimorfismo

- ***Abstract Base Classes*** (***ABCs***), ou ***Classes Abstratas***, em **Python** são classes que **não podem ser instanciadas diretamente**, mas são projetadas para serem **subclasses de outras classes**.

- Elas são usadas para **definir uma interface comum** que outras classes devem implementar.

- As **ABCs** são uma ferramenta poderosa na **Programação Orientada a Objetos** em **Python**, especialmente em relação à **herança** e ao **polimorfismo**.


### Herança

- As **ABCs** em **Python** são frequentemente usadas como **classes base para outras classes**.

- Uma **classe** que **herda** de uma **ABC** deve **implementar** **todos** os **métodos abstratos definidos na ABC**. Isso garante que **todas** as **subclasses** tenham uma **interface comum**.

- A **herança** é útil para **reutilização de código** e para definir **relações hierárquicas** entre classes.


#### Exemplo de ABC e Herança:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

# Como definimos o método abstrato `fazer_som`, todas as subclasses
# de `Animal` devem implementar esse método.

class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

# Nenhuma instância direta de Animal é permitida
# animal = Animal()  # Isso resultaria em um erro

# No entanto, instâncias das subclasses são permitidas
cachorro = Cachorro()
cachorro.fazer_som()  # Saída: Au au!
```


### Polimorfismo

- As **ABCs** em **Python** também facilitam a implementação do **polimorfismo**.

- Como as **subclasses** de uma **ABC** implementam uma **interface comum**, você pode **tratar diferentes objetos de subclasses da mesma maneira**, chamando os **mesmos métodos**.

- Isso é útil quando você tem uma **lista de objetos de diferentes tipos**, mas com **métodos em comum** que você deseja **chamar de forma uniforme**.


#### Exemplo de ABC e Polimorfismo:

- Considere as classes definidas no exemplo anterior.

```python
def fazer_som_em_todos(animais):
    for animal in animais:
        animal.fazer_som()

# Lista de diferentes tipos de animais
animais = [Cachorro(), Gato()]

# Chama o método fazer_som() em cada animal
fazer_som_em_todos(animais)
# Saída:
# Au au!
# Miau!

```

### Benefícios das Classes Abstratas

- **Garantia de Interface**:
	- As ABCs garantem que todas as subclasses implementem métodos específicos, fornecendo uma interface consistente.

- **Documentação Clara**:
	- As ABCs servem como uma documentação clara sobre quais métodos uma classe deve implementar para ser considerada de um tipo específico.

- **Facilita o Polimorfismo**:
	- O uso de ABCs simplifica o polimorfismo, permitindo que diferentes objetos sejam tratados de maneira uniforme, desde que implementem os métodos definidos na ABC.


## Aplicando na Solução do Desafio

- Para resolver o desafio, vamos então utilizar os conceitos de **classes abstratas**, **herança** e **polimorfismo** comentados anteriormente.

### Classe Abstrata para Fontes de Dados

- Vamos criar uma **classe abstrata** (**ABC**) para uma **fonte genérica de dados**.

```python
from abc import ABC, abstractmethod


class AbstractDataSource(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_data(self):
        msg = 'Not implemented.'
        raise NotImplementedError(msg)

    @abstractmethod
    def update_full_dataframe(self):
        msg = 'Not implemented.'
        raise NotImplementedError(msg)

    @abstractmethod
    def save_data(self):
        msg = 'Not implemented.'
        raise NotImplementedError(msg)

    @abstractmethod
    def update_data(self):
        msg = 'Not implemented.'
        raise NotImplementedError(msg)
```

- Com isso, definimos a **interface básica** que todas as nossas classes devem implementar.


### Classe para Fontes de Dados em Arquivos

- Agora, vamos criar uma **classe genérica** para **consumir dados** contidos em **arquivos** (sem uma extensão definida) na nossa **própria máquina**.

```python
from pathlib import Path

import pandas as pd
from source_classes.AbstractDataSource import AbstractDataSource


class FileSource(AbstractDataSource):
    def __init__(self, folder_name: str, extension: str) -> None:
        self.folder_name = folder_name
        self.extension = extension
        self.input_path: Path = self.get_or_create_input_path()
        self.processed_files = set()
        self.dataframe_queue = []
        self.new_dataframe = pd.DataFrame()
        self.full_dataframe = pd.DataFrame()

    def get_or_create_input_path(self) -> Path:
        input_path = Path('..') / 'data' / self.folder_name

        if not input_path.exists():
            input_path.mkdir(parents=True)

        return input_path

    def check_for_new_files(self) -> list[Path]:
        return [
            file_path
            for file_path in self.input_path.iterdir()
            if file_path not in self.processed_files
            and file_path.suffix == self.extension
        ]

    def get_data(self, file_paths: list[Path]) -> None:
        pass

    def update_full_dataframe(self) -> None:
        self.new_dataframe = pd.concat(
	        self.dataframe_queue, ignore_index=True
	    )
        self.dataframe_queue.clear()

        self.full_dataframe = pd.concat(
            [self.full_dataframe, self.new_dataframe],
            ignore_index=True,
        )

    def save_data(self, filename: str = 'consolidated.csv') -> None:
        file_path = Path('..') / 'data' / filename

        if not file_path.exists():
            self.new_dataframe.to_csv(file_path, index=False)
        else:
            self.new_dataframe.to_csv(
                file_path, mode='a', sep=',', index=False, header=False,
            )

        self.new_dataframe = pd.DataFrame()

    def update_data(self):
        new_files = self.check_for_new_files()

        if new_files:
            print('New files detected:')
            print(new_files)
            self.get_data(new_files)
            self.update_full_dataframe()
            self.save_data()
            print('New data saved successfully.')
        else:
            print('There are no new files.')

    def show_processed_files(self):
        print(self.processed_files)
```

- Veja que nossa classe **`FileSource`** herda da classe abstrata **`AbstractDataSource`**, criada anteriormente. Portanto, deve implementar os métodos abstratos que foram definidos.

- No **construtor** da classe **`FileSource`**, recebemos o nome da pasta (**`folder_name`**) onde estarão armazenados os arquivos que serão monitorados, assim como suas extensões (**`extension`**).

- Então, caso ainda não exista, criamos um **diretório** de onde serão lidos os **arquivos de entrada** (**`input_path`**), conforme o nome da pasta desejado. Caso já exista, `input_path` guarda o caminho completo até o diretório de entrada. Esse procedimento é realizado no método **`get_or_create_input_path`**.

- Finalmente, criamos algumas **estruturas de dados** necessárias para o funcionamento do nosso projeto.

	- **`processed_files`** é um conjunto onde armazenaremos cada arquivo que já foi processado, para evitar que um mesmo arquivo seja processado mais de uma vez.

	- **`dataframe_queue`** é uma lista temporária onde são armazenados os dataframes criados a partir de cada novo arquivo identificado no diretório de entrada. Posteriormente, esses dataframes serão incorporados a um dataframe e a um arquivo de saída com os dados consolidados.

	- **`new_dataframe`** é simplesmente um dataframe que concatena os dataframes em `dataframe_queue` a cada nova rodada.

	- **`full_dataframe`** é o dataframe consolidado contendo todos os dados dos arquivos no diretório de entrada.

- No método **`check_for_new_files`**, verificamos se existem novos arquivos no diretório de entrada, considerando que estes ainda não tenham sido processados e que possuam a extensão definida. O método retorna uma lista com os caminhos dos arquivos novos.

- O próximo passo deve acontecer no método **`get_data`**, onde é feita a leitura dos arquivos encontrados.

	- Como o processo de leitura depende da extensão dos arquivos, implementaremos esse método nas classes de cada extensão particular.

	- No entanto, ressalta-se que esse método é responsável por popular a lista **`dataframe_queue`** de dataframes a serem processados.

- No método **`update_full_dataframe`**, concatenamos os dataframes criados recentemente, presentes na lista **`dataframe_queue`**, e salvamos o resultado em **`new_dataframe`**. Finalmente, os incorporamos ao dataframe consolidado **`full_dataframe`**.

- No método **`save_data`**, continuamente incorporamos cada novo conjunto de dados lido a um arquivo **`.csv`** consolidado. Isso é feito usando o dataframe temporário **`new_dataframe`**.

- O último método, **`update_data`**, é responsável por orquestrar todos os processos mencionados acima:

	- Verificar se existem novos arquivos no diretório de entrada usando o método **`check_for_new_files`**.

	- Caso novos arquivos tenham sido identificados:

		- Fazer a leitura desses arquivos com o método **`get_data`**.

		- Atualizar o dataframe consolidados (**`full_dataframe`**) com o método **`update_full_dataframe`**.

		- Salvar os novos dados no arquivo **`.csv`** consolidado, usando o método **`save_data`**.

### Classe para Fontes de Dados em Arquivos CSV

- Como mencionado anteriormente, a classe **`FileSources`** é **genérica** e serve apenas como **modelo** para **classes específicas** de **extensões particulares de arquivos**.

- Assim, criamos uma nova **classe herdeira** de **`FileSources`** para lidar especificamente com **arquivos `.csv`**.

```python
from pathlib import Path

import pandas as pd
from source_classes.FileSource import FileSource


class CSVSource(FileSource):
    def __init__(
            self,
            folder_name: str = 'csv_files',
            extension: str = '.csv',
        ) -> None:
        super().__init__(folder_name, extension)

    def get_data(self, file_paths: list[Path]) -> None:
        for file in file_paths:
            try:
                self.dataframe_queue.append(pd.read_csv(file))
                self.processed_files.add(file)
            except Exception as e:
                print(f'An error occurred while trying to read {file}.')
                print(e)
                continue
```

- No **construtor** da classe **`CSVSource`**, apenas definimos **valores padrão** para os parâmetros **`folder_name`** e **`extension`**, para refletir especificamente que estamos lidando com arquivos **`.csv`**. Então, usamos a função **`super()`** para "aproveitar" o construtor da classe **`FileSource`**.

- Então, definimos o método **`get_data`** para fazer a leitura de uma lista de arquivos de entrada. Usamos a biblioteca **pandas** para ler os arquivos **`.csv`** e transformar cada um em um dataframe.

	- Os dataframes criados são armazenados na lista temporária **`dataframe_queue`** e os arquivos correspondentes são adicionados ao conjunto de arquivos processados **`processed_files`**.

> Note como foi possível **aproveitar** a **estrutura definida** na classe **`FileSource`**, 
tornando a implementação dessa nova classe mais simples.


### Classe para Fontes de Dados em Arquivos TXT

- De forma semelhante, criamos uma classe para lidar com arquivos com a extensão `.txt`, consideranto que contenham dados tabulados, ou seja, separados por `\t`.

```python
from pathlib import Path

import pandas as pd
from source_classes.FileSource import FileSource


class TXTSource(FileSource):
    def __init__(
            self,
            folder_name: str = 'txt_files',
            extension: str = '.txt',
        ) -> None:
        super().__init__(folder_name, extension)

    def get_data(self, file_paths: list[Path]) -> None:
        for file in file_paths:
            try:
                # Assume the .txt files are tabulated
                self.dataframe_queue.append(pd.read_csv(file, sep='\t'))
                self.processed_files.add(file)
            except Exception as e:
                print(f'An error occurred while trying to read {file}.')
                print(e)
                continue
```

- A classe **`TXTSource`** se assemelha bastante à classe **`CSVSource`**, uma vez que também só foi necessário **redefinir** o **construtor** e **implementar** o método **`get_data`**.

> Com isso, fica evidente a **facilidade** que o uso de **classes abstratas**, **herança** e **polimorfismo** nos **proporcionam** no desenvolvimento de **projetos**.

### Usando as Classes para Monitorar os Arquivos

- Agora, basta usar as classes definidas para fazer o monitoramento dos arquivos `.csv` e `.txt` da empresa.

- Então, criamos o seguinte arquivo **`main.py`**, responsável por executar nossas tarefas.


```python
import time

import schedule
from source_classes.CSVSource import CSVSource
from source_classes.TXTSource import TXTSource


def update_data(sources: list) -> None:
    for source in sources:
        source.update_data()

sources = [CSVSource(), TXTSource()]

schedule.every(10).seconds.do(update_data, sources=sources)

while True:
    schedule.run_pending()
    time.sleep(1)
```

- Usamos a biblioteca [**`schedule`**](https://schedule.readthedocs.io/en/stable/) para executar a cada 10 segundos a função **`update_data`**, que chama os métodos **`update_data`** de cada instância criada das classes **`CSVSource`** e **`TXTSource`**.

## Novo Desafio - Arquivos JSON

- Agora, temos um novo desafio.

- Além de monitorar arquivos `.csv` e `.txt`, também precisamos monitorar e ler arquivos no formato `.json` armazenados em outra pasta dedicada.


### Solução do Novo Desafio

- Vamos aproveitar toda a estrutura já construída com as classes `AbstractDataSource` e `FileSource` para criar rapidamente uma classe para fazer a leitura de arquivos `.json`.

- Assim, criamos a seguinte classe `JSONSource`.


```python
import json
from pathlib import Path

import pandas as pd
from source_classes.FileSource import FileSource


class JSONSource(FileSource):
    def __init__(
            self,
            folder_name: str = 'json_files',
            extension: str = '.json',
        ) -> None:
        super().__init__(folder_name, extension)

    def get_data(self, file_paths: list[Path]) -> None:
        for file in file_paths:
            try:
                with file.open('r', encoding='utf-8') as f:
                    self.dataframe_queue.append(
	                    pd.DataFrame(json.load(f))
	                )

                self.processed_files.add(file)
            except Exception as e:
                print(f'An error occurred while trying to read {file}.')
                print(e)
                continue
```

- Novamente, só foi necessário alterar o **construtor** da classe e implementar o método **`get_data`**, que é específico para arquivos **`.json`**.

- Agora, alteramos nosso arquivo **`main.py`** para **incluir** o **monitoramento** de **arquivos `.json`**. Para isso, basta **adicionar** uma **instância** da classe **`JSONSource`** à lista de fontes **`sources`**.


```python
import time

import schedule
from source_classes.CSVSource import CSVSource
from source_classes.JSONSource import JSONSource
from source_classes.TXTSource import TXTSource


def update_data(sources: list) -> None:
    for source in sources:
        source.update_data()


sources = [CSVSource(), TXTSource(), JSONSource()]

schedule.every(10).seconds.do(update_data, sources=sources)

while True:
    schedule.run_pending()
    time.sleep(1)
```

## Código Completo do Desafio

- O código completo da solução do desafio pode ser encontrado na pasta [`src`](https://github.com/kaiodt/bootcamp-data-eng/tree/main/aulas_13_14/src).
