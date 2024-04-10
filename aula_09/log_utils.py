import time
from functools import wraps
from sys import stdout

from loguru import logger

logger.remove()

logger.add(
    stdout,
    level='INFO',
)

logger.add(
    'pipeline_debug_log.log',
    level='DEBUG',
)

logger.add(
    'pipeline_info_log.log',
    level='INFO',
)


def logger_wraps(*, inputs=True, output=True, level='DEBUG'):
    def wrapper(func):
        name = func.__name__

        @wraps(func)
        def wrapped(*args, **kwargs):
            logger_ = logger.opt(depth=1)

            if inputs:
                logger_.log(
                    level,
                    "Executando função '{}' (args = {}, kwargs = {})",
                    name,
                    args,
                    kwargs,
                )

            try:
                result = func(*args, **kwargs)

                if output:
                    logger_.log(
                        level,
                        "Finalizando função '{}' (result = {})",
                        name,
                        result,
                    )

            except Exception:
                logger_.exception("Exceção capturada em '{}'.", name)
                raise

            else:
                return result

        return wrapped

    return wrapper


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(
            f"Função '{func.__name__}' executada em "
            f'{end_time - start_time:.4f} segundos.',
        )
        return result

    return wrapper
