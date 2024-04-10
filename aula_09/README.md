# Aula 09 - Funções em Python e Estruturas de Dados - Parte 3

- Nesta aula, continuaremos o estudo das **funções** em **Python**, introduzindo o conceito de **decoradores** e sua **aplicação** para gerar **logs de execução** de **programas**.


## Decoradores

- Em **Python**, um **decorador** é uma **função** que **envolve** **outra função**, **adicionando** **funcionalidade** a ela.

- **Decoradores** permitem **modificar** ou **estender** o **comportamento** de **funções** ou **métodos** de forma transparente e **reutilizável**.

- Eles são comumente usados para **adicionar** **funcionalidades** como:

	- Logging
	- Temporização
	- Autenticação
	- Controle de acesso
	- Caching

#### Exemplo 01

```python
def my_decorator(func):
    def wrapper():
        print('Antes de chamar a função')
        func()
        print('Depois de chamar a função')
    return wrapper

@my_decorator
def decorated_function():
    print('Função decorada')

decorated_function()

# Output:
# Antes de chamar a função
# Função decorada
# Depois de chamar a função
```

- Neste exemplo, **`my_decorator`** é uma **função decoradora** que **recebe** uma outra **função** (**`func`**) como **argumento**.

- Ela **define** uma **nova função** **`wrapper`**, que **envolve** a **chamada** da **função original** (**`func`**), **adicionando funcionalidade** **antes** e **depois** dela.

- O **decorador** então **retorna** essa **nova função** **`wrapper`**.

- Posteriormente, ao **usar** o **decorador** **`@my_decorator`** acima da **definição** da **função** **`decorated_function`**, estamos essencialmente **aplicando** o **decorador** à **função**.

- Quando **chamamos** **`decorated_function()`**, ela será automaticamente **envolvida** pela **função** **`wrapper`**, resultando na **impressão** de **`Antes de chamar a função`**, seguido pela **execução** da **função original** (**`func`**), e então **`Depois de chamar a função`**.


#### Exemplo 02

- Decoradores também podem aceitar argumentos. Aqui está um exemplo disso:

```python
def decorator_with_argument(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'O argumento passado é: {arg}')
            func(*args, **kwargs)
        return wrapper
    return decorator


@decorator_with_argument('Argumento_decorador')
def decorated_function_with_args(x, y):
    print(f'A soma de {x} e {y} é {x + y}.')

decorated_function_with_args(3, 5)

# Output:
# O argumento passado é: Argumento_decorador
# A soma de 3 e 5 é 8.
```

- Aqui, **`decorator_with_argument`** é uma **função** que **aceita** um **argumento** (**`arg`**) e **retorna** um **decorador**, que por sua vez **envolve** a **função original** e imprime o argumento passado antes de chamar a função.

- Ao **aplicar** **`@decorator_with_argument('Argumento_decorador')`**, o **argumento** é **passado** para a **função decoradora**.

- Quando **chamamos** **`decorated_function_with_args(3, 5)`**, ele **imprimirá** **`O argumento passado é: Argumento_decorador`** antes de executar a função decorada.


### Preservando Metadados de Funções

- Quando criamos um **decorador** que envolve uma função em outra função, os **metadados** da **função original**, como seu **nome**, **docstring** e outras propriedades, **podem** ser **perdidos**.

- A **função utilitária** **`functools.wraps`**, do **pacote** **`functools`** ajuda a **resolver** esse **problema**, **garantindo** que os **metadados** da **função original** sejam **preservados** na **função decorada**.


#### Exemplo 03

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Antes da função')
        result = func(*args, **kwargs)
        print('Depois da função')
        return result
    return wrapper


@decorator
def my_func():
    """Esta é a docstring da função."""
    print('Função decorada')


print(my_func.__name__)  # Output: my_func
print(my_func.__doc__)   # Output: Esta é a docstring da função.
```

- Neste exemplo, a função **`decorator`** é um **decorador** que **envolve** outra **função** **em torno** da **função original** (**`func`**).

- **Dentro** do **decorador**, usamos **`functools.wraps(func)`** para **garantir** que os **metadados** da **função original** sejam **copiados** para a **função decorada** **`wrapper`**.

- Isso inclui o **nome da função** (**`__name__`**) e a **docstring** (**`__doc__`**).

- Se **não** **usássemos** **`functools.wraps`**, a **função decorada** **perderia** esses **metadados** da função original, o que pode levar a **confusões** durante a **depuração** ou ao usar **ferramentas** que **dependem** dessas **informações**, como **ferramentas de documentação automática**.

> Usar **`functools.wraps`** é uma **prática recomendada** ao **criar** **decoradores** em **Python**, pois ajuda a manter a **integridade** dos **metadados** das funções originais.


## Logging

- **Logging** é uma **técnica** **fundamental** em programação para **registrar** **mensagens** relevantes **durante** a **execução** de um **programa**. É útil para **rastrear** o **fluxo** de **execução**, **depurar problemas**, **registrar** **eventos** importantes e **monitorar** o **desempenho** do programa.

- **Logging** é crucial para **desenvolvimento** e **manutenção** de **software**, pois **permite** aos desenvolvedores e administradores de sistema **entender** o que o **programa** está **fazendo**, **diagnosticar problemas** e **monitorar** o **desempenho** em **produção**.


## Loguru

- O **[Loguru](https://loguru.readthedocs.io/en/stable/index.html)** é uma **biblioteca** de **logging** para **Python** que visa trazer uma **experiência de uso** mais **simples** e **poderosa**, comparada ao módulo de logging padrão do Python.

- Com uma **API simples**, o **Loguru** oferece várias **funcionalidades** úteis, como **rotação de arquivos**, **serialização JSON**, **envio de mensagens** para **múltiplos destinos**, e muito mais. Tudo isso **sem** a necessidade de **configuração inicial complicada**.

- Podemos **instalar** o **Loguru** usando o **Poetry**:

	```bash
	poetry add loguru
	```

#### Exemplo 01 - Logging Básico


```python
from loguru import logger

logger.info('Isso é uma mensagem informativa')

# Output:
# 2024-04-09 17:22:43.186 | INFO     | __main__:<module>:61 - Isso é uma mensagem informativa
```

- Neste exemplo, fazemos o **log** de uma **mensagem informativa**, que é **exibida** apenas no **console**.


#### Exemplo 02 - Configuração de Arquivo de Log

```python
from loguru import logger

# Configurando o arquivo de log com rotação de 5MB
logger.add('meu_app.log', rotation='5 MB')

logger.info('Essa mensagem será salva no arquivo')

# Output:
# 2024-04-09 17:24:52.941 | INFO     | __main__:<module>:72 - Essa mensagem será salva no arquivo
```

- Aqui, usamos a função **`logger.add()`** para **configur** o **Loguru** para **salvar mensagens** de **log** no **arquivo** **`meu_app.log`**.

- Além disso, usamos a **opção** **`rotation`**, que determina que um **novo arquivo** será **criado** sempre que o **atual** **atingir** **5 MB**.


#### Exemplo 03 - Capturando e Salvando

```python
from sys import stderr
from loguru import logger

# Configuração do logger para exibir logs no stderr e salvar em arquivo,
# com filtragem e formatação específicas

logger.add(
    sink=stderr,
    format='{time} <r>{level}</r> <g>{message}</g> {file}',
    level='INFO',
)

logger.add(
    'meu_arquivo_de_logs.log',
    format='{time} {level} {message} {file}',
    level='INFO',
)

logger.info('Este é um log de informação.')
logger.error('Este é um log de erro.')

# Output:
# 2024-04-09T17:38:53.375967-0300 INFO Este é um log de informação. aula_09.py
# 2024-04-09 17:38:53.375 | ERROR    | __main__:<module>:98 - Este é um log de erro.
# 2024-04-09T17:38:53.375967-0300 ERROR Este é um log de erro. aula_09.py
```

- Neste código, **dois** "**sinks**" são **adicionados** ao **`logger`**:

	- **`stderr`,** para **exibir** os **logs**, com uma **formatação** específica que inclui o **tempo**, **nível de log**, **mensagem** e **arquivo de origem**.

	- **`'meu_arquivo_de_logs.log'`**, para **salvar** os **logs** em um **arquivo** com uma **formatação** que também inclui **tempo**, **nível**, **mensagem** e **arquivo de origem**.


## Níveis de Log

- Os **níveis de log** em **Python** (e em muitos sistemas de logging em outras linguagens de programação) são usados para **indicar** a **gravidade** ou **importância** das **mensagens** registradas pelo aplicativo.

- Eles ajudam a **diferenciar** entre **tipos de informações** que estão sendo **logadas**, permitindo uma **filtragem** e **análise** mais **eficazes** dos dados de log.

- A seguir, são **listados** os **níveis de log** mais comuns, em **ordem crescente de gravidade**.


### DEBUG

- **Descrição**:
	- O nível **DEBUG** é usado para **informações detalhadas**, tipicamente de interesse apenas quando se está **diagnosticando problemas**.

- **Uso**:
	- Desenvolvedores usam este nível para **obter informações detalhadas** sobre o **fluxo da aplicação**, **variáveis de estado**, e para **entender** como o **código** está **operando** durante o **desenvolvimento** e a **depuração**.


### INFO

- **Descrição**:
	- O nível **INFO** é usado para **confirmar** que as **coisas** estão **funcionando** **conforme** o **esperado**.

- **Uso**:
	- Este nível é **geralmente** o **padrão** em **produção** para **registrar** **eventos** **normais** do sistema, como **processos de inicialização**, **operações concluídas com sucesso**, ou outras **transações de rotina**.


### WARNING

- **Descrição**:
	- O nível **WARNING** indica que **algo** **inesperado** **aconteceu**, ou indica **algum problema** no **futuro próximo** (e.g., 'disco quase cheio'). O **software** está **funcionando** como **esperado**.

- **Uso**:
	- Utiliza-se este nível para **alertar** sobre **situações** que **podem** **necessitar** de **atenção** mas **não** **impedem** o **funcionamento** do sistema.
	- Por exemplo, usar uma **função obsoleta** ou **problemas de performance** que não requerem uma ação imediata.


### ERROR

- **Descrição**:
	- O nível **ERROR** indica que devido a um **problema mais grave**, a **execução** de alguma **função** ou **operação** **falhou**.

- **Uso**:
	- Este nível é usado para **registrar** **eventos de erro** que **afetam** a **operação** de uma **parte** do **sistema** ou **funcionalidade**, mas **não** **necessariamente** o **sistema** como um **todo**.
	- **Erros** que são **capturados** e **gerenciados** ainda podem ser **logados** neste **nível**.


### CRITICAL

- **Descrição**:
	- O nível **CRITICAL** indica um **erro grave** que **impede** a **continuação** da **execução** do **programa**.

- **Uso**:
	- É usado para **erros** que **necessitam** de **atenção imediata**, como um **falha crítica** no **sistema** que pode **resultar** em **parada total** do **serviço** ou **aplicação**.
	- Este nível deve ser **reservado** para os **problemas** mais **sérios**.


### Utilizando os Níveis

- A **seleção** do **nível de log** adequado para diferentes mensagens **permite** que os desenvolvedores e administradores de sistema configurem os logs para **capturar** **apenas** as **informações** de que **precisam**.

- Por exemplo, em um **ambiente de desenvolvimento**, você pode querer ver **todos** os **logs**, desde **DEBUG** até **CRITICAL**, para **entender** **completamente** o **comportamento** da **aplicação**.

- Em contraste, em um **ambiente de produção**, você pode configurar para **registrar** **apenas** **WARNING**, **ERROR**, e **CRITICAL**, para **reduzir** o **volume de dados** gerados e se **concentrar** em **problemas** que **necessitam** de **atenção**.


#### Exemplo 04 - Capturando Exceções com Log

```python
from loguru import logger

def my_function():
    raise ValueError('Um erro aconteceu!')

try:
    my_function()
except Exception:
    logger.exception('Uma exceção foi capturada')

# Output:
# 2024-04-09 17:54:25.804 | ERROR    | __main__:<module>:113 - Uma exceção foi capturada
# Traceback (most recent call last):
# ...
```

- Usando **`logger.exception()`**, **Loguru** automaticamente **captura** e **loga** o **traceback** da **exceção**, o que é extremamente **útil** para **diagnóstico de erros**.


## Logging com Decoradores

- Agora, vamos criar um **decorador** utilizando o **Loguru** para **adicionar** automaticamente **logs** a **qualquer** **função**.

- Isso nos **permite** **registrar automaticamente** quando uma **função** é **chamada** e quando ela **termina**, junto com qualquer **informação** **relevante**, como **argumentos** da função e o **resultado** **retornado** (ou **exceção** **lançada**).


#### Exemplo 05 - Logging com Decoradores

```python
from functools import wraps
from sys import stderr

from loguru import logger


logger.remove()

logger.add(
    sink=stderr,
    format='{time} <r>{level}</r> <g>{message}</g> {file}',
    level='INFO',
)

logger.add(
    'meu_arquivo_de_logs.log',
    format='{time} {level} {message} {file}',
    level='INFO',
)


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(
            f"Chamando função '{func.__name__}' com "
            f"args = {args} e kwargs = {kwargs}",
        )

        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")

        except Exception as e:
            logger.exception(
                f"Exceção capturada em '{func.__name__}': {e}"
            )

            # Relançar a exceção para não alterar o comportamento da
            # função decorada
            raise

        else:
            return result

    return wrapper


@log_decorator
def soma(a, b):
    return a + b


@log_decorator
def falha():
    raise ValueError('Um erro intencional')


# Testando as funções decoradas

soma(5, 3)  # Isso irá logar a chamada e o retorno

try:
    falha()  # Isso irá logar a chamada e a exceção
except ValueError:
    pass  # Ignora a exceção para fins de demonstração
```

- Ao **decorar** as **funções** **`soma`** e **`falha`** com **`@log_decorator`**, automaticamente **logamos** a **entrada** e **saída** (ou **exceção**) dessas **funções** sem alterar o corpo delas.

- Isso é especialmente **útil** para **debugar**, **monitorar** a **performance** de aplicações ou simplesmente **manter** um **registro** de quais **funções** estão sendo **chamadas** e com quais **argumentos**.

### Benefícios do Uso de Decoradores com Loguru

- O uso de **decoradores** em **conjunto** com o **Loguru** fornece uma **abordagem** **elegante** e **poderosa** para **adicionar** **logs** a **aplicações** **Python**.

- **Sem** a **necessidade** de **modificar** o **corpo da função**, podemos facilmente **adicionar** **funcionalidades** de **logging**, o que torna o **código** mais **limpo**, mantém a **separação de preocupações** e **facilita** a **manutenção** e o **debugging**.

- Além disso, ao **centralizar** a **lógica** de **logging** no **decorador**, promovemos a **reutilização** de **código** e garantimos uma **forma** **consistente** de **logar** **informações** em **diferentes** **partes** de uma **aplicação**.


## Temporização com Decoradores

- Um outro **uso** **recorrente** de **decoradores** é para fazer **temporização** de **funções**.

- Cria-se um **decorador** que **marca** o **tempo** entre o **início** da **execução** de uma **função** até sua **conclusão**.

- O código a seguir apresenta um **exemplo** de implementação dessa funcionalidade.


```python
import time
from loguru import logger
from functools import wraps


# Decorador de medida de tempo
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Função '{func.__name__}' executada em {end_time - start_time:.4f} segundos")
        return result
    return wrapper
```

## Padrão Singleton com Decoradores

- O **padrão** **Singleton** é um **padrão de design** que visa **garantir** que uma **classe** tenha **apenas** **uma instância** e forneça um **ponto de acesso global** para essa **instância**.

- Ele é útil em situações onde você deseja ter **exatamente uma instância de uma classe** em **todo** o seu **programa**, como por exemplo para **gerenciadores de configurações**, **pools de conexão**, **caches**, entre outros.

- Uma abordagem comum de implementação desse padrão em Python é usar um decorador.

---

- A seguir, temos um exemplo de uso do padrão Singleton para criar uma conexão única com um banco de dados:

```python
def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        print('Nova instância da conexão com o banco de dados.')

# Testando o padrão Singleton
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(f"db1 é db2? {'Sim' if db1 is db2 else 'Não'}")  # Output: Sim
```

## Desafio

- Integre no projeto de ETL da [Aula 08](https://github.com/kaiodt/bootcamp-data-eng/tree/main/aula_08) os decoradores para logging e temporização.


### Solução

- Confira os arquivos [`schema.py`](https://github.com/kaiodt/bootcamp-data-eng/blob/main/aula_09/schema.py), [`log_utils.py`](https://github.com/kaiodt/bootcamp-data-eng/blob/main/aula_09/log_utils.py), [`etl.py`](https://github.com/kaiodt/bootcamp-data-eng/blob/main/aula_09/etl.py) e [`pipeline.py`](https://github.com/kaiodt/bootcamp-data-eng/blob/main/aula_09/pipeline.py).
