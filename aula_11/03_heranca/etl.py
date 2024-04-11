import pandas as pd


class ETLProcess:
    def __init__(self, fonte_dados):
        self.fonte_dados = fonte_dados

    def extrair_dados(self):
        msg = 'Este método deve ser implementado nas classes filhas.'
        raise NotImplementedError(msg)

    def transformar_dados(self, dados):
        msg = 'Este método deve ser implementado nas classes filhas.'
        raise NotImplementedError(msg)

    def carregar_dados(self, dados_transformados):
        msg = 'Este método deve ser implementado nas classes filhas.'
        raise NotImplementedError(msg)

    def executar_etl(self):
        dados_extraidos = self.extrair_dados()
        dados_transformados = self.transformar_dados(dados_extraidos)
        self.carregar_dados(dados_transformados)


class ETLCSV(ETLProcess):
    def extrair_dados(self) -> pd.DataFrame:
        return pd.read_csv(self.fonte_dados)

    def transformar_dados(self, dados: pd.DataFrame) -> pd.DataFrame:
        # Exemplo simples de transformação: Converter todas as letras em
        # maiúsculas
        return dados.map(lambda x: x.lower() if isinstance(x, str) else x)

    def carregar_dados(self, dados_transformados: pd.DataFrame) -> None:
        # Lógica para carregar os dados transformados
        print('Dados transformados:')
        print(dados_transformados)


# Exemplo de uso
if __name__ == '__main__':
    fonte_csv = '../data/exemplo.csv'
    etl_csv = ETLCSV(fonte_csv)
    etl_csv.executar_etl()
