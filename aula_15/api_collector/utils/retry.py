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
