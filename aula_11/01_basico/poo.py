import pandas as pd


class ProcessadorCSV:
    def __init__(self, arquivo_csv: str) -> None:
        self.arquivo_csv = arquivo_csv
        self.df: pd.DataFrame

    def carregar_csv(self):
        # Carregar arquivo CSV em um DataFrame
        self.df = pd.read_csv(self.arquivo_csv)

    def remover_celulas_vazias(self):
        # Remover células vazias
        self.df = self.df.dropna()

    def filtrar_por_estado(self, estado: str) -> None:
        # Filtrar linhas pela coluna 'estado'
        self.df = self.df[self.df['estado'] == estado]

    def processar(self, estado: str) -> pd.DataFrame:
        # Carregar CSV, romover células vazias e filtrar por estado
        self.carregar_csv()
        self.remover_celulas_vazias()
        self.filtrar_por_estado(estado)

        return self.df


# Exemplo de uso
arquivo_csv = '../data/exemplo.csv'
estado_filtrado = 'SP'

processador = ProcessadorCSV(arquivo_csv)
df_filtrado = processador.processar(estado=estado_filtrado)

print(df_filtrado)
