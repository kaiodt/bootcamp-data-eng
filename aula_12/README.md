# Aula 12 - Introdução às Classes em Python

- Nesta aula, faremos uma **revisão** sobre os conceitos básicos de **Programação Orientada a Objetos** (**POO**) em **Python**.


## Programação Orientada a Objetos em Python

- Vamos considerar um problema em que precisamos ler arquivos `csv` e realizar uma filtragem de seus registros com base em critérios aplicados em uma coluna.


### Solução com Programação Funcional


- Inicialmente, vamos solucionar o problema usando **programação funcional**.

```python
import pandas as pd


def carregar_csv(arquivo_csv: str) -> pd.DataFrame:
    return pd.read_csv(arquivo_csv)


def filtrar_por_estado(df: pd.DataFrame, estado: str) -> pd.DataFrame:
    return df.loc[df['estado'] == estado]


def filtrar_por_preco(df: pd.DataFrame, preco: str) -> pd.DataFrame:
    return df.loc[df['preço'] == preco]


# Exemplo de uso
arquivo_csv = 'exemplo.csv'
estado = 'SP'
preco = '10,50'

df = carregar_csv(arquivo_csv)
print(df, '\n\n')

# Output:
#    id  preço estado        data
# 0   1  10,50     SP  20/01/2024
# 1   2  10,48     RJ  20/01/2024
# 2   3  10,55     MG  19/01/2024
# 3   4  10,75     MT  25/01/2024
# 4   5  10,39     SP  19/01/2024
# 5   6  11,00     MA  21/01/2024
# 6   7  10,50     SP  22/01/2024
# 7   8  10,50     DF  22/01/2024

df_filtrado_estado = filtrar_por_estado(df, estado)
print(df_filtrado_estado, '\n\n')

# Output:
#    id  preço estado        data
# 0   1  10,50     SP  20/01/2024
# 4   5  10,39     SP  19/01/2024
# 6   7  10,50     SP  22/01/2024

df_filtrado_preco = filtrar_por_preco(df_filtrado_estado, preco)
print(df_filtrado_preco, '\n\n')

# Output:
#    id  preço estado        data
# 0   1  10,50     SP  20/01/2024
# 6   7  10,50     SP  22/01/2024
```

- Note que a solução é relativamente **simples**, sendo adequada caso este procedimento **não** **precise** ser **executado diversas vezes**, nem precise de muitas **alterações nas funcionalidades**.


### Solução com POO

- Agora, vamos resolver o mesmo problema usando **programação orientada a objetos**.

```python
import pandas as pd


class CSVProcessor:
    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv
        self.df_raw: pd.DataFrame
        self.df_processado: pd.DataFrame

    def carregar_arquivo(self):
        self.df_raw = pd.read_csv(self.arquivo_csv)
        self.df_processado = self.df_raw.copy()
        return self.df_raw

    def filtrar_por_coluna(self, coluna, valor):
        self.df_processado = self.df_processado.loc[
            self.df_processado[coluna] == valor
        ]
        return self.df_processado

    def reset_df_processado(self):
        self.df_processado = self.df_raw.copy()
        return self.df_processado
```

- **Usando** a **classe** criada:
```python
from sol_poo import CSVProcessor

arquivo_csv = 'exemplo.csv'
processor = CSVProcessor(arquivo_csv)

df = processor.carregar_arquivo()
print(df, '\n\n')

# Output:
#    id  preço estado        data
# 0   1  10,50     SP  20/01/2024
# 1   2  10,48     RJ  20/01/2024
# 2   3  10,55     MG  19/01/2024
# 3   4  10,75     MT  25/01/2024
# 4   5  10,39     SP  19/01/2024
# 5   6  11,00     MA  21/01/2024
# 6   7  10,50     SP  22/01/2024
# 7   8  10,50     DF  22/01/2024

df_filtrado_estado = processor.filtrar_por_coluna(coluna='estado', valor='SP')
print(df_filtrado_estado, '\n\n')

# Output:
#    id  preço estado        data
# 0   1  10,50     SP  20/01/2024
# 4   5  10,39     SP  19/01/2024
# 6   7  10,50     SP  22/01/2024

df_filtrado_preco = processor.filtrar_por_coluna(coluna='preço', valor='10,50')
print(df_filtrado_preco, '\n\n')

# Output:
#    id  preço estado        data
# 0   1  10,50     SP  20/01/2024
# 6   7  10,50     SP  22/01/2024

processor.reset_df_processado()

df_filtrado_estado = processor.filtrar_por_coluna(coluna='estado', valor='DF')
print(df_filtrado_estado, '\n\n')

# Output:
#    id  preço estado        data
# 7   8  10,50     DF  22/01/2024
```

- Veja que obtivemos os **mesmos resultados**, porém, para este exemplo simples, a **implementação** usando **POO** parece um pouco **mais complexa**.

- Entretanto, esta **solução** é mais **modular** e pode ser **expandida** de maneira mais **fácil**.
