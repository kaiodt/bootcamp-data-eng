# Aula 17 - SQLAlchemy - Conjunto de Ferramentas para Manipular SQL em Python

- Nesta aula, vamos introduzir a biblioteca **SQLAlchemy**, que fornece um conjunto de soluções para **manipulação de bancos de dados** em **Python**.


## Introdução ao SQLAlchemy

- [**SQLAlchemy**](https://www.sqlalchemy.org/) é uma **biblioteca** **Python** de **Object-Relational Mapping** (**ORM**) extremamente popular e poderosa.


### Principais Funcionalidades do SQLAlchemy

- **ORM (Object-Relational Mapping)**:
    - O SQLAlchemy fornece um conjunto abrangente de ferramentas para **mapear objetos Python** para **tabelas** em um **banco de dados relacional**.
    - Com isso, podemos **manipular dados** armazenados em um banco de dados usando um **código em Python**, em vez de escrever diretamente em SQL.

- **Abordagem Declarativa e Core**:
    - O SQLAlchemy oferece duas **interfaces** principais:
        - Declarativa
        - Core
    
    - A abordagem **declarativa** nos permite definir **modelos de dados** (**classes** Python) que são automaticamente **mapeados** para **tabelas** no **banco de dados**. Essa abordagem é **mais expressiva** e semelhante à forma como os modelos são definidos em outras bibliotecas de ORM.
    
    - O **core** fornece uma **API** de **nível mais baixo** para **interagir** com o **banco de dados** usando **SQL nativo**. Isso oferece **mais flexibilidade** para construir **consultas complexas** e executar **operações avançadas** no banco de dados.

- **Operações CRUD**:
    - O SQLAlchemy simplifica as operações **CRUD** (Create, Read, Update, Delete) em bancos de dados relacionais. Ele fornece **métodos simples e intuitivos** para **criar**, **ler**, **atualizar** e **excluir** **registros** usando objetos Python, sem a necessidade de escrever SQL manualmente.

- **Suporte a várias engines de banco de dados**:
	- O SQLAlchemy é **compatível** com uma **ampla gama de engines** de banco de dados SQL, incluindo **SQLite**, **PostgreSQL**, **MySQL**, **Oracle** e **SQL Server**. Assim, podemos escolher a engine de banco de dados que melhor atenda às necessidades do projeto.

- **Gerenciamento de transações e sessões**:
    - O SQLAlchemy oferece recursos avançados para gerenciamento de transações e sessões, incluindo **controle de isolamento**, **commit** e **rollback de transações**, e **gerenciamento de contexto** para **sessões** de banco de dados.

- **Relacionamentos entre tabelas**:
    - O SQLAlchemy permite **definir relacionamentos complexos entre tabelas** do banco de dados usando **chaves estrangeiras** e **associações**. Isso simplifica a navegação entre objetos relacionados e facilita a consulta de dados em estruturas de dados complexas.


## Usando o SQLAlchemy
- A seguir, temos alguns **exemplos de uso** da biblioteca **SQLAlchemy**.


### Conectando a um Banco de Dados SQLite

- O código a seguir cria uma **engine de conexão** com um **banco de dados SQLite** em memória:

```python
from sqlalchemy import create_engine

# Conectar ao banco SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Conexão com banco SQLite estabelecida.")
```

### Criando uma Tabela a partir de um Modelo

- Com o código a seguir, usamos a **abordagem declarativa** (**`declarative_base`**) para criar um **modelo** (classe **`Usuario`**), que **mapeia** a **tabela** **`usuarios`**  em nosso **banco de dados**.

- Para **materializar** a **tabela** no banco, usamos **método** **`Base.metadata.create_all(engine)`**, que recebe nossa **engine de conexão** com o banco de dados com **argumento**.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Conectar ao banco SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)
```

### Inserindo Registros na Tabela

- Para **inserir registros na tabela** que criamos, ou em uma tabela já existente, primeiro precisamos **criar uma instância da classe** que representa a tabela em questão. Em seguida, devemos **criar uma sessão** para a conexão com o banco de dados.

```python
from sqlalchemy.orm import sessionmaker

# Criando uma sessão (assumindo que a engine foi criada)
Session = sessionmaker(bind=engine)
session = Session()

# Adicionando um registro de usuário
# Aqui, não estamos usando um gerenciador de contexto (NÃO RECOMENDADO!)
new_user = Usuario(nome='Kaio', idade=30)
session.add(new_user)
session.commit()
print('Usuário inserido com sucesso.')
```

- Após criar uma instância da classe `Usuario`, basta usar os métodos **`add`** e **`commit`** para **executar** a **adição** no banco de dados.

- Entretanto, também é necessário **verificar** se a **transação** foi **concluída** com sucesso, caso contrário, é preciso **desfazer** as outras **transações** da sessão (**rollback**). Além disso, também é necessário **encerrar** a **sessão** ao final das transações, independente de terem sido completadas ou não.

```python
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

# Criando uma sessão (assumindo que a engine foi criada)
Session = sessionmaker(bind=engine)
session = Session()

try:
    new_user = Usuario(nome='Maria', idade=28)
    session.add(new_user)
    session.commit()
    print('Usuário inserido com sucesso.')

except SQLAlchemyError as e:
    session.rollback()
    print('Erro ao inserir usuário.')
    print(e)
finally:
    session.close()
```

- Embora a versão acima esteja correta, a melhor forma de realizar essas transações é utilizando um **gerenciador de contexto** do Python (**`with`**), pois garantimos que a sessão sempre será encerrada.

```python
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

try:
    with Session() as session:
        new_user = Usuario(nome='João', idade=35)
        session.add(new_user)
        session.commit()
        print('Usuário inserido com sucesso.')
except SQLAlchemyError as e:
    print('Erro ao inserir usuário.')
    print(e)
```

### Fazendo uma Consulta na Tabela

- Agora, vamos fazer uma consulta na tabela e verificar a inserção de um dos registros.

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

with Session() as session:
	user = session.query(Usuario).filter_by(nome='Kaio').first()
	if user:
		print(f'Usuário encontrado: {user.nome}, Idade: {user.idade}')
	else:
		print('Usuário não encontrado')
```

- Note que também é possível usar **filtros** (cláusula **`WHERE`**) na **query** e **limitar a quantidade de resultados** (**`first`** traz apenas o **primeiro resultado** da busca).


## Desafio

- Neste desafio, criaremos duas **tabelas relacionadas**, `Produto` e `Fornecedor`, utilizando **SQLAlchemy**.

- Cada produto terá um fornecedor associado, demonstrando o uso de **chaves estrangeiras** para estabelecer **relações** entre tabelas. Além disso, realizaremos **inserções** nessas tabelas para praticar a manipulação de dados.


### Definindo os Modelos e Criando as Tabelas

- Primeiramente, vamos **definir os modelos** das nossas entidades e **criar as tabelas** correspondentes no **banco de dados SQLite**.

```python
from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Fornecedor(Base):
    __tablename__ = 'fornecedores'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))


class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Float)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    fornecedor = relationship('Fornecedor')


engine = create_engine('sqlite:///:memory:', echo=True)

# Criando tabelas
Base.metadata.create_all(engine)
```

- Note como foi estabelecido o **relacionamento** entre as **tabelas** **`fornecedores`** e **`produtos`**.

### Inserindo Registros nas Tabelas

- Agora, vamos **inserir** alguns **registros** nas tabelas de **fornecedores** e de **produtos**.

```python
# Criando sessão
Session = sessionmaker(engine)

# Inserindo fornecedores
try:
    with Session() as session:
        fornecedores = [
            Fornecedor(
                nome='Fornecedor A',
                telefone='12345678',
                email='contato@a.com',
                endereco='Endereço A',
            ),
            Fornecedor(
                nome='Fornecedor B',
                telefone='87654321',
                email='contato@b.com',
                endereco='Endereço B',
            ),
            Fornecedor(
                nome='Fornecedor C',
                telefone='12348765',
                email='contato@c.com',
                endereco='Endereço C',
            ),
            Fornecedor(
                nome='Fornecedor D',
                telefone='56781234',
                email='contato@d.com',
                endereco='Endereço D',
            ),
            Fornecedor(
                nome='Fornecedor E',
                telefone='43217865',
                email='contato@e.com',
                endereco='Endereço E',
            ),
        ]
        session.add_all(fornecedores)
        session.commit()
        print('Fornecedores inseridos com sucesso.')
except SQLAlchemyError as e:
    print('Erro ao inserir fornecedores:')
    print(e)

# Inserindo produtos
try:
    with Session() as session:
        produtos = [
            Produto(
                nome='Produto 1',
                descricao='Descrição do Produto 1',
                preco=100.10,
                fornecedor_id=1,
            ),
            Produto(
                nome='Produto 2',
                descricao='Descrição do Produto 2',
                preco=200.20,
                fornecedor_id=2,
            ),
            Produto(
                nome='Produto 3',
                descricao='Descrição do Produto 3',
                preco=300.30,
                fornecedor_id=3,
            ),
            Produto(
                nome='Produto 4',
                descricao='Descrição do Produto 4',
                preco=400.40,
                fornecedor_id=4,
            ),
            Produto(
                nome='Produto 5',
                descricao='Descrição do Produto 5',
                preco=500.50,
                fornecedor_id=5,
            ),
        ]
        session.add_all(produtos)
        session.commit()
        print('Produtos inseridos com sucesso.')
except SQLAlchemyError as e:
    print('Erro ao inserir produtos:')
    print(e)
```

### Consultando os Registros Inseridos

- Para **verificar** que os **registros** foram **inseridos**, vamos fazer uma **consulta** à **tabela de produtos**:

```python
with Session() as session:
    for produto in session.query(Produto).all():
        if produto:
            print(
                f'Produto: {produto.nome}, '
                f'Fornecedor: {produto.fornecedor.nome}',
            )
```

- O código deve **retornar** a **listagem de produtos** cadastrados, exibindo seus **nomes** e respectivos **fornecedores**.

### Realizando uma Consulta com JOIN e GROUP BY

- Agora, vamos criar uma **query** que envolve as **operações** de **`JOIN`** e **`GROUP BY`** de **SQL**.

- Queremos utilizar o **SQLAlchemy** para **reproduzir** a seguinte **query** **SQL**:

	```SQL
	SELECT
		f.nome,
		SUM(p.preco) AS preco_total
	FROM
		produtos p
		JOIN fornecedores f ON p.fornecedor_id = fornecedores.id
	GROUP BY
		f.nome;
	```

- O código a seguir mostra como podemos obter o mesmo resultado da query acima usando o **SQLAlchemy**:

```python
from sqlalchemy import func

with Session() as session:
    resultado = (
        session
        .query(
            Fornecedor.nome,
            func.sum(Produto.preco).label('preco_total'),
        )
        .join(
            Produto, Fornecedor.id == Produto.fornecedor_id,
        )
        .group_by(
            Fornecedor.nome,
        )
        .all()
    )
  
    if resultado:
        for fornecedor, preco_total in resultado:
            print(
	            f'Fornecedor: {fornecedor}, '
	            f'Preço Total: {preco_total:.2f}'
	        )
```

- Utilizamos o método **`query`** para construir uma consulta que **seleciona** o nome do fornecedor e a soma dos preços dos produtos, calculada com **`func.sum`**.

- Usamos **`join`** para **juntar** as tabelas `Produto` e `Fornecedor` com base na chave estrangeira `fornecedor_id`.

- O método **`group_by`** foi então utilizado para **agrupar** os resultados pelo nome do fornecedor.


### Solução do Desafio

- O código completo da solução do desafio pode ser encontrado no arquivo [`desafio.py`](https://github.com/kaiodt/bootcamp-data-eng/blob/main/aula_17/desafio.py).