# Aula 19 - O que é uma API - Criando Nossa Primeira API

- Nesta aula, vamos continuar nos **aprofundando** nos conceitos sobre **APIs**. Mais especificamente, vamos **criar uma API** em **Python** usando a **biblioteca FastAPI**. Essa API se **integrará** a um **banco de dados SQLite** usando a **biblioteca SQLAlchemy**, de forma que possamos realizar todas as **operações** de **CRUD**.

- Adicionalmente, vamos criar um **container Docker** para nossa **aplicação** e fazer um **deploy** da mesma na **plataforma Render**.


## APIs em Python com FastAPI

- Como visto na [Aula 15](https://github.com/kaiodt/bootcamp-data-eng/tree/main/aula_15), [**FastAPI**](https://fastapi.tiangolo.com/) é uma **biblioteca de desenvolvimento web** rápida, moderna e fácil de usar para **criar APIs** em **Python**. Ela é construída sobre o **framework ASGI** (**Asynchronous Server Gateway Interface**).

- Uma das características mais poderosas do **FastAPI** é a **geração automática de documentação** interativa para sua **API**.

	- Basta acessar **`/docs`** ou **`/redoc`** na URL do servidor para ver a documentação gerada automaticamente com base nas definições da sua API.

- Além disso, o **FastAPI** se **integra** ao [**Pydantic**](https://docs.pydantic.dev/latest/) para realizar **validação de dados** de forma **automática**.


### Exemplo de API Básica usando FastAPI

- Primeiramente, precisamos **instalar** a biblioteca **`fastapi`** e um **servidor ASGI**, como o **`uvicorn`**.

- Em seguida, podemos criar uma aplicação **FastAPI** simplesmente importando a classe **`FastAPI`** do módulo **`fastapi`**:

	```python
	from fastapi import FastAPI
	
	app = FastAPI()
	```

- Podemos **definir rotas** da API usando **decoradores**, que associam **funções Python** a **URLs específicos**. A função será executada sempre que a URL correspondente for acessada:

	```python
	@app.get("/hello")
	async def read_root():
	    return {"message": "Hello, world!"}
	```

- Também podemos **receber parâmetros** em uma rota, que serão passados para a função correspondente. O FastAPI pode **inferir** automaticamente os **tipos de dados** com base em **type hints**:

	```python
	@app.get("/items/{item_id}")
	async def read_item(item_id: int):
	    return {"item_id": item_id}
	```

- Para **iniciar** o **servidor ASGI `uvicorn`** e executar nossa aplicação, usamos o comando:

	```bash
	uvicorn main:app --reload
	```

	- Isso iniciará o servidor na URL **`http://127.0.0.1:8000`** e qualquer alteração nos arquivos será automaticamente recarregada.

	- Adicionalmente, podemos acessar a **documentação** (**Swagger UI**) criada automaticamente para essas duas rotas por meio da URL **`http://127.0.0.1:8000/docs`**.


## Criando um Sistema CRUD via API

- Agora, vamos criar uma **API** usando **FastAPI** para implementar um sistema **CRUD** (Create, Read, Update, Delete) que interage com um **banco de dados SQLite**.

- Para isso, vamos criar um **projeto** com a seguinte **estrutura**:

	```text
	api_crud
	├── database.py
	├── main.py
	├── models.py
	└── schemas.py
	```

### Inicializando o Poetry e Instalando as Dependências

- Para fazer a gestão de dependências da nossa aplicação, vamos usar o **Poetry**.

- Assim, dentro do diretório do projeto, execute o seguinte comando e preencha as informações solicitadas nos prompts.

	```bash
	poetry init
	```

- Em seguida, adicione as dependências da aplicação:

	```bash
	poetry add fastapi uvicorn sqlalchemy
	```

- Instale as dependências com o seguinte comando:

	```bash
	poetry install
	```

- Com isso, também será criado um ambiente virtual para o projeto.


### Configuração do Banco de Dados

- Inicialmente, vamos configurar os **componentes** relacionados à **interação** com o **banco de dados**.

- Vamos utilizar a biblioteca **SQLAlchemy** para criar e manipular um banco de dados **SQLite**.

- Então, criamos o seguinte arquivo **`database.py`**:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = 'sqlite:///api_crud_db.db'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine, autocommit=False, autoflush=False
)

Base = declarative_base()


def get_db():
    with SessionLocal() as session:
        yield session
```

- Com isso, criamos uma **engine de conexão** com o banco de dados, uma **função** que será utilizada para **criar sessões individuais** para **cada requisição** feita ao banco de dados, e o **objeto `Base`**, que será utilizado para criar os **modelos ORM das tabelas** do banco de dados.

### Criando os Modelos das Tabelas

- Agora, vamos criar os **modelos** para as **tabelas** do banco de dados.

- No caso, temos apenas uma **tabela de itens** (**`items`**). Cada item tem um **id** (chave primária), **nome**, **preço** e uma **flag** que indica se está em **oferta** ou não (`is_offer`).

- Então, criamos o seguinte arquivo **`models.py`**:

```python
from database import Base
from sqlalchemy import Boolean, Column, Float, Integer, String


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    price = Column(Float, nullable=False)
    is_offer = Column(Boolean, default=False)
```

- Veja que importamos o objeto `Base` do módulo `database.py` criado anteriormente.

- Também definimos algumas colunas como sendo índices, não nulas, ou com um valor padrão.


### Criando os Schemas do Pydantic

- Além de criar o modelo da tabela no banco de dados, também precisamos criar os **schemas** relacionados a ela dentro da nossa aplicação, a depender do **contexto** onde seus dados serão utilizados.

- Esses **schemas** são **criados** usando a **biblioteca Pydantic**, que realiza a **validação** dos dados juntamente com o **FastAPI**.

- No caso, criaremos um **schema de base** para os itens (**`ItemBase`**), com informações que são comuns entre os contextos, outro schema que será usado na **criação de um item** (**`ItemCreate`**), e um schema que traz **todas as informações** de um item contidas no **banco de dados**, inclusive seu id, que só fica disponível depois que o item é criado (**`Item`**).

- Assim, temos o seguinte arquivo **`schemas.py`**:

```python
from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    name: str
    price: float
    is_offer: bool = False


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
```

- Note que os schemas `ItemCreate` e `Item` herdam do schema `ItemBase`, que é nosso schema de base.

- O schema `ItemCreate` tem os mesmos atributos que `ItemBase`. Entretanto, é comum que existam atributos que são específicos da criação de um objeto (por exemplo, a senha original de um usuário).

- Já o schema `Item`, além de ter os atributos de `ItemBase`, tem também o `id`, uma vez que, depois de criar um item, este já terá um id atribuído.

- No schema `Item`, também adicionamos a configuração `from_attributes=True`. Isso permite que o Pydantic consiga ler um modelo ORM.


### Criando as Rotas da API com as Funções de CRUD

- Após criar os modelos e schemas, agora vamos criar as rotas da API, uma para cada operação de CRUD (Create, Read, Update, Delete) no banco de dados.

- Criamos então o seguinte arquivo `main.py`:

```python
from typing import Annotated

import models
import schemas
from database import engine, get_db
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# Create tables
models.Base.metadata.create_all(bind=engine)

# Create app
app = FastAPI()

# Database section dependency
CurrentSession = Annotated[Session, Depends(get_db)]


@app.post('/items/', response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: CurrentSession):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get('/items/', response_model=list[schemas.Item])
def get_items(db: CurrentSession, skip: int = 0, limit: int = 10):
    return db.query(models.Item).offset(skip).limit(limit).all()


@app.get('/items/{item_id}', response_model=schemas.Item)
def get_item(item_id: int, db: CurrentSession):
    db_item = (
	    db
	    .query(models.Item)
	    .filter(models.Item.id == item_id)
	    .first()
	 )

    if not db_item:
        raise HTTPException(status_code=404, detail='Item not found.')

    return db_item


@app.put('/items/{item_id}', response_model=schemas.Item)
def update_item(
	item_id: int,
	item: schemas.ItemCreate,
	db: CurrentSession
):
    db_item = (
	    db
	    .query(models.Item)
	    .filter(models.Item.id == item_id)
	    .first()
	)

    if not db_item:
        raise HTTPException(status_code=404, detail='Item not found.')

    for key, value in item.model_dump().items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item


@app.delete('/item/{item_id}', response_model=schemas.Item)
def delete_item(item_id: int, db: CurrentSession):
    db_item = (
	    db
	    .query(models.Item)
	    .filter(models.Item.id == item_id)
	    .first()
	)

    if not db_item:
        raise HTTPException(status_code=404, detail='Item not found.')

    db.delete(db_item)
    db.commit()
    return db_item
```

- Com o comando `models.Base.metadata.create_all(bind=engine)`, nós **criamos** a(s) **tabela(s)** no **banco de dados**, caso ainda não existam, conforme definido nas classes no arquivo **`models.py`**.

- Em seguida, **criamos** nossa **aplicação** com o comando `app = FastAPI()`.

- Então, definimos uma **dependência** para as nossas funções, que consiste na **criação** de uma **sessão independente** para cada **interação** com o **banco de dados**. Essa dependência é definida com o comando `CurrentSession = Annotated[Session, Depends(get_db)]`, onde `get_db` é uma função criada no arquivo `database.py`.

- Com isso, podemos **definir** nossas **rotas**, uma para cada operação de **CRUD**. Note que basta adicionar um **decorador** nas **funções** dependendo da operação envolvida, seguindo as **correspondências**:

	- Create --> POST
	- Read --> GET
	- Update --> PUT
	- Delete --> DELETE

- Note também que, em cada função, definimos o **argumento** **`db`**, que é justamente a **dependência** de **sessão** que criamos anteriormente. Esse processo é chamado de **injeção de dependência** (**dependency injection**).


### Testando a Aplicação

- Para **testar a aplicação**, inicializamos o **servidor `uvicorn`** com o seguinte comando:

	```bash
	uvicorn main:app --reload
	```

- Então, acessamos a **documentação automática** (**Swagger UI**) da nossa API na URL `http://127.0.0.1:8000/docs`.

- Assim, é possível testar cada uma das rotas definidas.


### Criando uma Imagem Docker para a API

- Para facilitar o **deploy** da nossa **aplicação**, vamos criar uma **imagem** de **container** **Docker** com seu código.

- Então, criamos o seguinte **`Dockerfile`** um diretório acima do diretório da aplicação (`api_crud`):

```dockerfile
FROM python:3.12

# Instalando Poetry
RUN pip install poetry

# Copiar o código fonte da aplicação
COPY . /api_crud

# Definir diretório de trabalho
WORKDIR /api_crud

# Instalar dependências com poetry
RUN poetry install

# Expor a porta da aplicação
EXPOSE 8501

# Definir entrypoint para executar o servidor uvicorn
ENTRYPOINT [ "poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8501"]
```

### Fazendo o Deploy da Aplicação

- Para fazer o **deploy** da aplicação, é necessário **criar** um **repositório remoto** (por exemplo, no **GitHub**) para o código.

- Depois, podemos utilizar um **serviço de hospedagem** como o [**Render**](https://render.com/), que consegue se **conectar** a esse **repositório remoto**, identificar o **`Dockerfile`** e fazer o **deploy**.


## Código Completo

- O código completo da aplicação pode ser encontrado na pasta [`api_crud`](https://github.com/kaiodt/bootcamp-data-eng/tree/main/aula_19/api_crud).
