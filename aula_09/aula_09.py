##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 09 - Funções em Python e Estruturas de Dados - Parte 3                #
##############################################################################


# Decoradores #################################################################


# Exemplo simples -------------------------------------------------------------


def my_decorator(func):
    def wrapper():
        print('Antes da função')
        func()
        print('Depois da função')
    return wrapper


@my_decorator
def decorated_function():
    print('Função decorada')


decorated_function()

print()


# Exemplo com argumentos ------------------------------------------------------


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

print()


# Preservando metadados de funções --------------------------------------------


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


print(my_func.__name__)  # Output: my_func
print(my_func.__doc__)   # Output: Esta é a docstring da função.

print()


# Logging com Loguru ##########################################################


# Logging básico --------------------------------------------------------------


from loguru import logger

logger.info('Isso é uma mensagem informativa')

print()


# Configuração de arquivo de log ----------------------------------------------


# Configurando o arquivo de log com rotação de 5MB
logger.add('meu_app.log', rotation='5 MB')

logger.info('Essa mensagem será salva no arquivo')

print()


# Capturando e salvando -------------------------------------------------------


from sys import stderr

# Configuração do logger para exibir logs no stderr e salvar em arquivo, com
# filtragem e formatação específicas

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

print()


# Capturando exceções com log -------------------------------------------------


def my_function():
    raise ValueError('Um erro aconteceu!')


try:
    my_function()
except Exception:
    logger.exception('Uma exceção foi capturada')

print()


# Logging com decoradores -----------------------------------------------------

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
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")

            # Relançar a exceção para não alterar o comportamento da função
            # decorada
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

soma(5, 3)  # Isso irá logar a chamada e o retorno

try:
    falha()  # Isso irá logar a chamada e a exceção
except ValueError:
    pass  # Ignora a exceção para fins de demonstração


# Temporização com Decoradores ################################################

import time
from functools import wraps

from loguru import logger


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


@measure_time
def count(secs):
    print(f'Contando {secs} segundos...')
    time.sleep(secs)
    print('Fim.')


count(5)

print()


# Padrão Singleton com Decoradores ############################################


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
