from etl import pipeline_consolidaded_sales

DATA_PATH = 'data'

pipeline_consolidaded_sales(
    data_path=DATA_PATH,
    export_filename='dados',
    export_file_formats=['csv', 'parquet'],
)
