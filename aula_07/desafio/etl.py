import csv
from pathlib import Path


def read_csv(path_to_csv: str) -> list[dict]:
    """Lê um arquivo csv e retorna uma lista de dicionários com cada linha.

    Parameters:
        path_to_csv: Caminho para o arquivo csv a ser lido.

    Returns:
        Uma lista de dicionários onde cada dicionário corresponde a uma linha
        do arquivo csv.
    """
    with Path.open(path_to_csv, encoding='utf-8') as file:
        return list(csv.DictReader(file))


def group_by_category(
    product_list: list[dict],
) -> dict[str, list[dict]]:
    """Recebe uma lista de produtos (dicionários) e os agrupa por categoria.

    Parameters:
        product_list: Lista de dicionários, cada um correspondendo a um
        produto.

    Returns:
        Um dicionário onde as chaves são as categorias e os valores são listas
        de dicionários, cada um correspondendo a um produto naquela categoria.
    """
    products_by_category = {}

    for product in product_list:
        category = product['Categoria']

        if category not in products_by_category:
            products_by_category[category] = []

        products_by_category[category].append(
            {
                'Produto': product['Produto'],
                'Quantidade': int(product['Quantidade']),
                'Venda': float(product['Venda']),
            },
        )

    return products_by_category


def compute_sales_by_category(
    products_by_category: dict[str, list[dict]],
) -> dict[str, float]:
    """Consolida as vendas de produtos por categoria.

    Parameters:
        products_by_category: Dicionário onde as chaves são as categorias e os
        valores são listas de dicionários, cada um correspondendo a um produto
        naquela categoria.

    Returns:
        Um dicionário onde as chaves são as categorias e os valores são o total
        de vendas naquela categoria.
    """
    sales_by_category = {}

    for category, products in products_by_category.items():
        sales_by_category[category] = sum(
            product['Quantidade'] * product['Venda'] for product in products
        )

    return sales_by_category


def run_pipeline(path_to_csv: str) -> None:
    product_list = read_csv(path_to_csv)
    products_by_category = group_by_category(product_list)
    sales_by_category = compute_sales_by_category(products_by_category)

    for category, total_sales in sales_by_category.items():
        print(f'{category}: $ {total_sales:.2f}')


if __name__ == '__main__':
    SALES_CSV_PATH = 'vendas.csv'

    run_pipeline(SALES_CSV_PATH)
