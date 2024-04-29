# Aula 15 - Conclusão de POO

- Nesta aula, concluímos o estudo de **Programação Orientada a Objetos** (**POO**) em **Python** focando no conceito de **encapsulamento**.

- Também serão apresentados **conceitos básicos** sobre **APIs**.


## O que são APIs?

- Uma ***API*** (***Application Programming Interface***) é um **conjunto de regras e protocolos** que permite que **diferentes softwares** se **comuniquem entre si**.

- A **API** define como diferentes **componentes de software** devem **interagir** uns com os outros.

- Dessa forma, as **APIs** permitem que **sistemas diferentes** se **comuniquem**, mesmo que sejam desenvolvidos por **empresas diferentes**, estejam em **plataformas distintas** ou usem **linguagens de programação diferentes**.

- Uma **API** também funciona como uma **camada de abstração** sobre as funcionalidades de um **sistema**. Assim, os **desenvolvedores** podem **interagir** com um **sistema** usando uma **API**, sem precisar entender os **detalhes internos** desse sistema.

- Normalmente, as **APIs** **especificam** os **padrões e formatos de dados** que serão usados para a **comunicação** entre sistemas, garantindo que os dados sejam transmitidos de maneira **consistente** e **compreensível** para ambas as partes.

- As **APIs** geralmente implementam **medidas de segurança** para **proteger** os **dados** e as **operações** do sistema. Isso pode incluir **autenticação**, **autorização**, **criptografia** e outras técnicas de segurança.


## REST APIs

- Uma ***REST API*** (***Representational State Transfer Application Programming Interface***) é um tipo de API que segue os princípios da **arquitetura REST**.


### Princípios da Arquitetura REST

- **Arquitetura Cliente-Servidor**:
	- Existe uma clara separação entre o cliente (que faz requisições) e o servidor (que processa essas requisições e fornece as respostas).

- **Stateless (Sem Estado)**:
	- Cada requisição do cliente para o servidor deve conter todas as informações necessárias para que o servidor entenda e processe a requisição.
	- O servidor não mantém nenhum estado da sessão do cliente entre requisições. Isso significa que cada requisição é tratada de forma independente, o que simplifica a escalabilidade e a tolerância a falhas.

- **Cacheabilidade**:
	- As respostas do servidor podem ser marcadas como cacheáveis ou não-cacheáveis. Isso permite que os clientes armazenem em cache as respostas para economizar largura de banda e melhorar o desempenho.

- **Interface Uniforme**:
	- Uma REST API expõe uma interface uniforme que permite que os clientes acessem e manipulem recursos de forma padronizada.
	- Isso geralmente é feito usando os métodos **HTTP** (**GET**, **POST**, **PUT**, **DELETE**) e **URLs** (**endpoints**) para identificar **recursos**.

- **Sistema de Camadas**:
	- Um sistema REST pode ser composto por várias camadas, onde cada camada tem uma responsabilidade específica. Isso permite que a arquitetura seja escalável e modular.


## APIs em Python com FastAPI

- Como de costume, existem bibliotecas em Python que nos permitem criar APIs facilmente.

- Uma delas é a [**FastAPI**](https://fastapi.tiangolo.com/) é uma **biblioteca de desenvolvimento web** rápida, moderna e fácil de usar para **criar APIs** em **Python**. Ela é construída sobre o **framework ASGI** (**Asynchronous Server Gateway Interface**).

- Uma das características mais poderosas do **FastAPI** é a **geração automática de documentação** interativa para sua **API**.
	- Basta acessar **`/docs`** ou **`/redoc`** na URL do servidor para ver a documentação gerada automaticamente com base nas definições da sua API.


### Exemplo Básico de API em Python usando FastAPI

- Primeiramente, precisamos **instalar** a biblioteca **`fastapi`** e um **servidor ASGI**, como o **`uvicorn`**.

- Em seguida, podemos criar uma aplicação **FastAPI** simplesmente importando a classe **`FastAPI`** do módulo **`fastapi`**:

	```python
	from fastapi import FastAPI
	
	app = FastAPI()
	```

- Podemos **definir rotas** da API usando **decoradores**, que associam funções Python a URLs específicos. A função será executada sempre que a URL correspondente for acessada:

	```python
	@app.get("/hello")
	def read_root():
	    return {"message": "Hello, world!"}
	```

- Também podemos **receber parâmetros** em uma rota, que serão passados para a função correspondente. O FastAPI pode **inferir** automaticamente os **tipos de dados** com base em **type hints**:

	```python
	@app.get("/items/{item_id}")
	def read_item(item_id: int):
	    return {"item_id": item_id}
	```

- Para **iniciar** o **servidor ASGI `uvicorn`** e executar nossa aplicação, usamos o comando:

	```bash
	uvicorn main:app --reload
	```

	- Isso iniciará o servidor na URL **`http://127.0.0.1:8000`** e qualquer alteração nos arquivos será automaticamente recarregada.


## Construindo uma API com FastAPI

- Como parte da aula, vamos criar uma **API simples** usando o **FastAPI** para simular uma API real que fornece informações sobre **compras de produtos**.

- A ideia é posteriormente criar uma **nova camada** que **consumirá** **dados** gerados por essa **API**.


### Criando Dados Fictícios com a Biblioteca Faker

- A biblioteca [**Faker**](https://faker.readthedocs.io/en/master/index.html) é bastante útil para **criação de dados fictícios** que podem ser utilizados para fazer **provas de conceito** de **aplicações**, ou mesmo criar dados para serem usados em **testes da aplicação**.

- O código a seguir foi desenvolvido para criar **dados fictícios** sobre **produtos**.
	- Para cada produto, temos um código de barras (EAN), um nome de produto e um preço.
	- Os dados gerados sobre os produtos são salvos em um arquivo `.csv`.

```python
import csv
import random

from faker import Faker

fake = Faker()


def generate_products(n_products: int) -> list[tuple[str, str, float]]:
    """Gera dados fictícios de determinado número de produtos."""
    products = []
    for _ in range(n_products):
        ean = fake.ean(length=13)
        product_name = f'{fake.word()} {fake.word()}'.title()
        price = round(random.uniform(10.0, 1000.0), 2)
        products.append((ean, product_name, price))
    return products


def save_products(
        products: list[tuple[str, str, float]],
        filename: str = 'data/products.csv',
    ) -> None:
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['EAN', 'Product Name', 'Price'])  # Header
        writer.writerows(products)  # Dados dos produtos


if __name__ == '__main__':
    save_products(
        products=generate_products(200),
        filename='product_data/products.csv',
    )
```

### Criando uma API que Gera Dados sobre Compras

- Após gerar uma listagem de produtos com o código anterior, vamos criar uma **API** que fornecerá **dados sobre compras** desses **produtos**.

```python
import random

import pandas as pd
from faker import Faker
from fastapi import FastAPI

app = FastAPI(debug=True)
fake = Faker()

input_filename = 'product_data/products.csv'
df = pd.read_csv(input_filename)


@app.get('/gerar_compra')
async def gerar_compra():
    product = df.sample(1).iloc[0]
    return [{
        'client': fake.name(),
        'creditcard': fake.credit_card_provider(),
        'product_name': product['Product Name'],
        'ean': int(product['EAN']),
        'price': round(product['Price'] * 1.1, 2),
        'client_position': fake.location_on_land(),
        'store': random.randint(1, 10),
        'datetime': fake.iso8601(),
    }]


@app.get('/gerar_compras/{numero_registros}')
async def gerar_compras(numero_registros: int) -> list[dict] | dict:
    if numero_registros < 1:
        return {'error': 'Número de registros deve ser no mínimo 1.'}

    compras = []
    for _ in range(numero_registros):
        product = df.sample(1).iloc[0]
        compras.append({
            'client': fake.name(),
            'creditcard': fake.credit_card_provider(),
            'product_name': product['Product Name'],
            'ean': int(product['EAN']),
            'price': round(product['Price'] * 1.1, 2),
            'client_position': fake.location_on_land(),
            'store': random.randint(1, 10),
            'datetime': fake.iso8601(),
        })

    return compras
```

- A rota **`/gerar_compra`** aciona a função **`gerar_compra`**, onde selecionamos aleatoriamente um dos produtos da listagem e criamos dados fictícios sobre sua compra usando a biblioteca **Faker**. A aplicação então retorna os dados sobre essa compra.

- Já a rota **`/gerar_compras/{numero_registros}`** aciona a função **`gerar_compras`**, que recebe como argumento um inteiro que representa o número de registros de compras que desejamos gerar. De forma semelhante à rota anterior, a função retorna uma lista de registros de compras, considerando que **`numero_registros`** é um valor maior ou igual a 1.

- Para testar a API localmente, usamos o comando:

	```bash
	uvicorn app:app --reload
	```

## Consumindo Dados da API e Salvando na Nuvem

- Após desenvolver nossa API, agora vamos **desenvolver** um **sistema** que **consome** dessa **API** e **salva** os **resultados** em um **bucket S3** na **AWS**.

- Vamos supor que só estejamos interessados em uma parte dos dados fornecidos pela API. Então, vamos criar um schema definindo que informações vamos considerar.

```python
GenericSchema = dict[str, str | float | int]

PurchaseSchema: GenericSchema = {
	'ean': int,
	'price': float,
	'store': int,
	'datetime': str,
}
```

- Nesse caso, estamos interessados no código de barras (`ean`), no preço do produto, na loja onde ocorreu a compra, e na data e hora da compra. Definimos isso com o **`PurchaseSchema`** usando **type hint** do Python.

---

- Adicionalmente, vamos criar um **decorator utilitário** que **tenta** **executar** uma **função** ou **método** um **determinado número de vezes**, conforme o código a seguir:

```python
import time
from functools import wraps


def retry(exception_to_check, tries=3, delay=1, backoff=2):
    """Decorator que retenta a função um número de vezes em caso de exceção.

    Parameters:
        exception_to_check: Exceção ou tupla de exceções capturadas.
        tries: Número máximo de tentativas.
        delay: Tempo inicial de espera entre as tentativas.
        backoff: Fator pelo qual o tempo de atraso aumenta a cada tentativa.
    """
    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            _tries, _delay = tries, delay

            while _tries > 1:
                try:
                    return func(*args, **kwargs)
                except exception_to_check as e:
                    print(f'{func.__name__} falhou.\n')
                    print(e)
                    print(f'\nTentando novamente em {_delay} segundos.')
                    print(f'Tentativas restantes: {_tries - 1}')
  
                    time.sleep(_delay)
                    _tries -= 1
                    _delay *= backoff

            return func(*args, **kwargs)
        return wrapper_retry
    return decorator_retry
```

---

- Também precisamos criar uma **interface com o bucket S3** na **AWS**. Para isso, criamos a classe **`S3Client`**:

```python
import os
import sys

import boto3
from botocore.exceptions import NoCredentialsError


class S3Client:
    def __init__(self):
        self._env = {
            'AWS_ACCESS_KEY_ID': os.environ.get('AWS_ACCESS_KEY_ID'),
            'AWS_SECRET_ACCESS_KEY': os.environ.get('AWS_SECRET_ACCESS_KEY'),
            'REGION_NAME': os.environ.get('REGION_NAME'),
            'S3_BUCKET': os.environ.get('S3_BUCKET'),
            'DATALAKE': os.environ.get('DATALAKE'),
        }

        for var, value in self._env.items():
            if value is None:
                print(f'A variável de ambiente {var} não foi definida.')
                sys.exit(1)

        self.s3 = boto3.client(
            's3',
            aws_access_key_id=self._env['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=self._env['AWS_SECRET_ACCESS_KEY'],
            region_name=self._env['REGION_NAME'],
        )

    def upload_file(self, data, s3_key):
        try:
            self.s3.put_object(
                Body=data.getvalue(),
                Bucket=self._env['S3_BUCKET'],
                Key=s3_key,
            )
        except NoCredentialsError:
            msg = (
                'Credenciais não encontradas. '
                'Certifique-se de configurar suas credenciais AWS corretamente'
            )
            print(msg)

    def download_file(self, s3_key):
        try:
            file = self.s3.get_object(
                Bucket=self._env['S3_BUCKET'],
                Key=s3_key,
            )
            print(f'Download bem-sucedido para {s3_key}.')
        except NoCredentialsError:
            msg = (
                'Credenciais não encontradas. '
                'Certifique-se de configurar suas credenciais AWS corretamente'
            )
            print(msg)
        except FileNotFoundError:
            msg = (
                f'Arquivo {s3_key} não encontrado no '
                f'bucket {self._env['S3_BUCKET']}.'
            )
            print(msg)
        except Exception as e:
            print('Ocorreu um erro durante o download:')
            print(e)
        else:
            return file

    def list_objects(self, prefix):
        return self.s3.list_objects(
            Bucket=self._env['S3_BUCKET'],
            Prefix=prefix,
        )['Contents']
```

- Note que é preciso **definir** as **credenciais** do **bucket S3** na **AWS** usando **variáveis de ambiente**.

---

- Em seguida, criamos a classe **`APICollector`**, que fará a **coleta** dos **dados** a partir da nossa **API** e os **salvará** no **bucket S3**.

```python
from datetime import datetime
from io import BytesIO

import pandas as pd
import requests
from utils.retry import retry


class APICollector:
    def __init__(self, schema, cloud, base_url='http://127.0.0.1:8000'):
        self._schema = schema
        self._cloud = cloud
        self._buffer = None
        self.base_url = base_url

    def start(self, num_purchases):
        response = self.get_data(num_purchases)
        purchases_list = self.extract_data(response)
        parquet_file = self.convert_to_parquet(purchases_list)

        if self._buffer is not None:
            filename = self.generate_filename()
            print(filename)
            self._cloud.upload_file(parquet_file, filename)
            return True

        return False

    @retry(requests.exceptions.RequestException, tries=5, delay=1, backoff=2)
    def get_data(self, num_purchases):
        if num_purchases > 1:
            response = requests.get(
                f'{self.base_url}/gerar_compras/{num_purchases}',
                timeout=10,
            ).json()
        else:
            response = requests.get(
                f'{self.base_url}/gerar_compra',
                timeout=10,
            ).json()
        return response

    def extract_data(self, response):
        purchases_list: list[self._schema] = []
  
        for item in response:
            item_dict = {}

            for key, data_type in self._schema.items():
                if isinstance(item.get(key), data_type):
                    item_dict[key] = item[key]
                else:
                    item_dict[key] = None

            purchases_list.append(item_dict)

        return purchases_list

    def convert_to_parquet(self, purchases_list):
        purchases_df = pd.DataFrame(purchases_list)

        self._buffer = BytesIO()

        try:
            with self._buffer as buffer:
                purchases_df.to_parquet(buffer)
                return buffer
        except Exception as e:
            print('Error converting DataFrame to parquet.')
            print(e)
            self._buffer = None

    @staticmethod
    def generate_filename():
        date_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return f'api/api_collected_purchases__{date_time}.parquet'
```

- É importante ressaltar que essa **classe** foi **desenvolvida** de **forma agnóstica** em relação à **cloud** utilizada. Em vez de um bucket S3, poderíamos ter uma **outra classe cliente** de **outra nuvem** e **utilizá-la da mesma maneira**.

- Aproveitando o conceito de **encapsulamento**, basta saber que a **classe da nuvem** em questão **deve ter um método `upload_file`**, **não** sendo **necessário** **saber nenhum detalhe interno** de sua **implementação**.

---

- Por fim, criamos um arquivo **`main.py`**, onde usamos a biblioteca `schedule` para fazer chamadas periódicas à API e armazenar os dados da resposta no bucket S3.

```python
import time

import schedule
from contracts.schemas import PurchaseSchema
from datasource.api import APICollector
from utils.aws.client import S3Client

schema = PurchaseSchema
cloud = S3Client()


def api_collector(schema, cloud, num_purchases):
    APICollector(schema, cloud).start(num_purchases)
    print('Executado')


schedule.every(1).minutes.do(
	api_collector, schema, cloud, num_purchases=50
)

while True:
    schedule.run_pending()
    time.sleep(1)
```

## Código Completo

- O código completo usado na aula pode ser encontrado nas pastas [`fake_api`](https://github.com/kaiodt/bootcamp-data-eng/tree/main/aula_15/fake_api) e [`api_collector`](https://github.com/kaiodt/bootcamp-data-eng/tree/main/aula_15/api_collector).