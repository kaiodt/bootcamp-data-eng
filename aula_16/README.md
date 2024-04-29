# Aula 16 - Revisão de POO e SQLModel

- Nesta aula, veremos como os conceitos de **POO** estão relacionados com a **interação** do **Python** com **bancos de dados**.

- Também serão abordados os conceitos sobre **operações CRUD** em **bancos de dados**, **ORM** e a biblioteca **SQLModel**.


## Operações CRUD em Bancos de Dados

- ***Operações CRUD*** são operações básicas que podem ser realizadas em um **banco de dados** ou em qualquer **sistema de armazenamento de dados**.

- O acrônimo **CRUD** significa:

	- **C**reate:
		- **Criar** novos registros ou entradas no banco de dados.
		- Isso geralmente é feito por meio de uma instrução **SQL** **`INSERT`**, que adiciona uma nova linha a uma tabela.

	- **R**ead:
		- **Ler** ou recuperar registros existentes do banco de dados.
		- Isso geralmente é feito por meio de uma instrução **SQL** **`SELECT`**, que recupera dados de uma ou mais tabelas com base em critérios especificados.

	- **U**pdate:
		- **Atualizar** registros existentes no banco de dados com novas informações.
		- Isso geralmente é feito por meio de uma instrução **SQL** **`UPDATE`**, que atualiza os valores de uma ou mais colunas em registros existentes com base em critérios especificados.

	- **D**elete:
		- **Excluir** registros existentes do banco de dados.
		- Isso geralmente é feito por meio de uma instrução **SQL** **`DELETE`**, que remove registros de uma tabela com base em critérios especificados.

- Essas operações formam a **base** para a **maioria das interações** com **bancos de dados** e são essenciais para a manipulação eficaz dos dados.


## Object-Relational Mapping (ORM)

- ***Object-Relational Mapping*** (***ORM***) é uma técnica de programação que permite aos desenvolvedores **manipular bancos de dados relacionais usando objetos de programação**.

- **ORM** **mapeia** as **tabelas do banco de dados** em **classes Python** e as **linhas** em **objetos**. Dessa forma, é possível usar conceitos de **programação orientada a objetos** para realizar **operações** no **banco de dados**.

- A **relação** entre **ORM** e as **operações CRUD** é **direta**, pois ORM simplifica muito a implementação dessas operações.

- Por exemplo, cada **operação CRUD** pode se relacionar com um **ORM** da seguinte forma:

	- **Create**:
		- Com ORM, **criar novos registros** no banco de dados é tão simples quanto **instanciar um objeto** da classe correspondente e chamando um **método de salvamento**, como `save()` ou `commit()`, a depender da biblioteca adotada.
		- O **ORM** se encarrega de **traduzir** essa **operação** em uma **instrução SQL** **`INSERT`** e **executá-la** no banco de dados.

	- **Read**:
		- Para realizar **operações de leitura**, podemos usar **métodos** fornecidos pelo **ORM** para **recuperar objetos** do banco de dados com base em **critérios especificados**.
		- Por exemplo, ao **invés** de escrever **instruções SQL** **`SELECT`**, você pode usar **métodos** como `filter()` ou `get()` para recuperar objetos que satisfaçam determinadas condições.

	- **Update**:
		- **Atualizar registros** existentes com **ORM** também é simples. É possível **modificar os atributos** de um **objeto** e, em seguida, chamar um **método de salvamento** para **persistir** essas **alterações** no banco de dados. O ORM cuidará de traduzir isso em uma **instrução SQL** **`UPDATE`**.

	- **Delete**:
		- Da mesma forma que com a operação de **atualização**, **excluir registros** com **ORM** envolve chamar um **método** específico para **remover um objeto do banco de dados**. O ORM traduzirá isso em uma **instrução SQL** **`DELETE`** apropriada.

- Além de **simplificar as operações CRUD**, **ORM** também oferece outras vantagens, como **abstração do sistema de banco de dados**, tornando o código mais agnóstico e independente em relação ao sistema adotado.

	- Com isso, é possível **alterar facilmente o sistema de banco de dados** utilizado sem modificar muito o código da aplicação.


## Biblioteca de ORM SQLModel

- [**SQLModel**](https://sqlmodel.tiangolo.com/) é uma **biblioteca Python** de **ORM** que oferece uma maneira simples e declarativa de interagir com bancos de dados relacionais.


### Principais Características do SQLModel

- **Declarativo e baseado em tipagem**:
	- SQLModel permite que você **defina modelos de dados** de forma **declarativa**, utilizando a **tipagem estática** do **Python** (**PEP 484**) para especificar os tipos de dados dos atributos dos modelos.

- **Integração com [Pydantic](https://docs.pydantic.dev/latest/)**:
	- SQLModel é construído sobre o **Pydantic**, que é uma biblioteca de **validação de dados**. Isso significa que os **modelos** do SQLModel são **automaticamente validados** e **serializados** usando as funcionalidades do **Pydantic**.

- **Suporte para CRUD**:
	- SQLModel facilita a realização das **operações CRUD** (Create, Read, Update, Delete) em bancos de dados relacionais. Ele fornece **métodos simples** para criar, ler, atualizar e excluir registros de forma eficiente.

- **Suporte a várias engines de banco de dados**:
	- SQLModel é **compatível** com **várias engines de banco de dados SQL**, incluindo **SQLite**, **PostgreSQL** e **MySQL**. Isso permite que você escolha a engine de banco de dados que melhor se adapta às necessidades do seu projeto.

- **Geração automática de schemas**:
	- SQLModel pode **gerar automaticamente** os **schemas** do **banco de dados** com base na definição dos modelos com classes em Python.

- **Suporte a consultas complexas**:
	- SQLModel oferece suporte a **consultas complexas** usando a **linguagem de consulta SQL padrão**. Ele fornece uma interface conveniente para construir consultas dinâmicas e realizar operações de **filtragem**, **ordenação** e **junção** de forma fácil e intuitiva.

- **Integração com frameworks web**:
	- SQLModel pode ser facilmente **integrado** com **frameworks web** populares, como **FastAPI** e **Flask**, para criar **aplicativos web** que **interagem** com **bancos de dados** de forma eficiente e segura.


## Usando a Biblioteca SQLModel

### Exemplo

- Vamos reproduzir o [**exemplo**](https://sqlmodel.tiangolo.com/#example) simples presente na **documentação** do **SQLModel**.

- Suponha que temos uma **tabela SQL** chamada `hero` com as seguintes **colunas**:

	- `id`
	- `name`
	- `secret_name`
	- `age`

- Desejamos que a **tabela** contenha os seguintes **dados**:

    | id  | name       | secret_name      | age  |
    | --- | ---------- | ---------------- | ---- |
    | 1   | Deadpond   | Dive Wilson      | null |
    | 2   | Spider-Boy | Pedro Parqueador | null |
    | 3   | Rusty-Man  | Tommy Sharp      | 48   |


### Criando o Modelo para a Tabela

- Para **criar** um **modelo** referente a nossa **tabela**, basta **criar** uma **classe** (**`Hero`**), que **herda** de **`SQLModel`**.

- Ao passar o **argumento** **`table=True`**, indicamos que queremos que a **tabela** seja **materializada** em um **banco de dados**.

- Dentro da classe, **definimos** as **colunas** e seus **tipos**, usando **type hints** do **Python**. Também podemos usar a **classe** **`Field`** para **definir** mais **detalhes** sobre uma **coluna**, por exemplo, indicá-la como **chave primária** da tabela.

```python
from typing import Optional

from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
```

### Criando Registros para a Tabela

- Para **criar registros** na nossa tabela, basta **criar instâncias** da **classe** `Hero`.

```python
hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
```

### Criando a Tabela e Adicionando os Registros em um Banco de Dados

- Para **materializar a tabela** no **banco de dados**, bem como **criar os registros**, primeiramente é necessário **criar uma engine** que se **conectará** ao **banco de dados** desejado.

- Por simplicidade, vamos considerar um **banco de dados SQLite**.

- Para **criar a tabela**, basta usar o **método** `SQLModel.metadata.create_all(engine)`.

- Então, para **criar os registros** na tabela, **abrimos** uma **sessão** (`Session`) e **adicionamos** cada **instância** criada anteriormente.

```python
from sqlmodel import Session, SQLModel, create_engine

engine = create_engine('sqlite:///database.db', echo=True)

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()
```

### Lendo Dados de uma Tabela

- Agora que criamos nossa tabela e adicionamos alguns registros, podemos fazer a **leitura** deles em uma nova sessão.

```python
from sqlmodel import select

with Session(engine) as session:
    statement = select(Hero).where(Hero.name == 'Spider-Boy')
    hero = session.exec(statement).first()
    print(hero)
```

- Também é possível **criar** uma **query** **manualmente**:

```python
from sqlmodel import text

with Session(engine) as session:
    statement = text('SELECT * FROM hero;')
    results = session.exec(statement).fetchall()
    print(results)
```
