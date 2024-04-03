import etl

SALES_CSV_PATH = 'vendas.csv'

product_list = etl.read_csv(SALES_CSV_PATH)
products_by_category = etl.group_by_category(product_list)
sales_by_category = etl.compute_sales_by_category(products_by_category)

for category, total_sales in sales_by_category.items():
    print(f'{category}: $ {total_sales:.2f}')
