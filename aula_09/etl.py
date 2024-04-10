from pathlib import Path
from typing import Literal

import pandas as pd
import pandera as pa
from log_utils import logger_wraps, measure_time
from schema import SalesSchema


@measure_time
@logger_wraps()
@pa.check_output(SalesSchema)
def extract_json_files_to_dataframe(data_path: str) -> pd.DataFrame:
    return pd.concat(
        (
            pd.read_json(json_file)
            for json_file in Path(data_path).glob('*.json')
        ),
        ignore_index=True,
    )


@measure_time
@logger_wraps()
def compute_total_sales(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['Total'] = df['Quantidade'] * df['Venda']
    return df


@measure_time
@logger_wraps()
def export_data(
    df: pd.DataFrame,
    filename: str,
    file_formats: list[Literal['csv', 'parquet']],
) -> None:
    for file_format in file_formats:
        if file_format.lower() == 'csv':
            df.to_csv(f'{filename}.csv', index=False)
        elif file_format.lower() == 'parquet':
            df.to_parquet(f'{filename}.parquet', index=False)
        else:
            print(
                f'Formato "{file_format}" é inválido. '
                'Use somente "csv" ou "parquet".',
            )


@measure_time
@logger_wraps()
def pipeline_consolidaded_sales(
    data_path: str,
    export_filename: str,
    export_file_formats: list[Literal['csv', 'parquet']],
) -> None:
    df_raw = extract_json_files_to_dataframe(data_path)
    df_transformed = compute_total_sales(df_raw)

    export_data(
        df_transformed,
        filename=export_filename,
        file_formats=export_file_formats,
    )
