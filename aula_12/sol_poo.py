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
