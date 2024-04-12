from sol_poo import CSVProcessor

arquivo_csv = 'exemplo.csv'
processor = CSVProcessor(arquivo_csv)

df = processor.carregar_arquivo()
print(df, '\n\n')

df_filtrado_estado = processor.filtrar_por_coluna(coluna='estado', valor='SP')
print(df_filtrado_estado, '\n\n')

df_filtrado_preco = processor.filtrar_por_coluna(coluna='preço', valor='10,50')
print(df_filtrado_preco, '\n\n')

processor.reset_df_processado()

df_filtrado_estado = processor.filtrar_por_coluna(coluna='estado', valor='DF')
print(df_filtrado_estado, '\n\n')
