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

df_filtrado_estado = filtrar_por_estado(df, estado)
print(df_filtrado_estado, '\n\n')

df_filtrado_preco = filtrar_por_preco(df_filtrado_estado, preco)
print(df_filtrado_preco, '\n\n')
