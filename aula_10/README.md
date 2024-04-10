# Aula 10 - Aula de Revisão e Dúvidas

## Temas Abordados


### Pyenv

- [**pyenv**](https://github.com/pyenv/pyenv) é uma ferramenta capaz de **gerenciar múltiplas versões** de **Python** em uma **máquina**, de forma que uma não interfira na outra.

- O **pyenv** é a **forma recomendada** de **instalar** **Python** em uma máquina.

- Permite **alterações rápidas** entre as **versões** de **Python** **instaladas**, possibilitando **selecionar** a **versão** desejada para cada **projeto**.

- É **essencial** **definir** a **versão de Python** que deve ser **usada** em um **projeto**. Com isso, **cria-se** um **ambiente determinístico**, que pode ser **reproduzido** por **outras** **pessoas**.

- Outro ponto importante é sempre **verificar** se a **versão** de **Python** utilizada em um **projeto** não está muito **defasada**, principalmente se não estiver mais sendo **atualizada**.


### Poetry

- Já o [**Poetry**](https://python-poetry.org/) é uma ferramenta de **gerenciamento de dependências** e **empacotamento**.

- Também é **essencial** para **geração** de **ambientes determinísticos** e **reprodutíveis**.

- O **Poetry** torna bem **fácil** a **adição** de **dependências** em um **projeto**, inclusive fazendo a **separação de contextos**, como **produção** e **desenvolvimento**.


### Decoradores

#### Preservando Metadados de Funções

- Quando criamos um **decorador** que envolve uma função em outra função, os **metadados** da **função original**, como seu **nome**, **docstring** e outras propriedades, **podem** ser **perdidos**.

- A **função utilitária** **`functools.wraps`**, do **pacote** **`functools`** ajuda a **resolver** esse **problema**, **garantindo** que os **metadados** da **função original** sejam **preservados** na **função decorada**.


#### Exemplo

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
