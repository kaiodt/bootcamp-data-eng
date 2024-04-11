import pandas as pd


def carregar_csv_e_filtrar(arquivo_csv, estado):
    # Carregar o arquivo CSV em um DataFrame
    df = pd.read_csv(arquivo_csv)

    # Verificar e remover células vazias
    df = df.dropna()

    # Filtrar as linhas pela coluna estado
    return df[df['estado'] == estado]


# Exemplo de uso
arquivo_csv = '../data/exemplo.csv'
estado_filtrado = 'SP'
df_filtrado = carregar_csv_e_filtrar(arquivo_csv, estado_filtrado)

print(df_filtrado)
