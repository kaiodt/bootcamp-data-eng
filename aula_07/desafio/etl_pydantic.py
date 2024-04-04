import csv
from pathlib import Path

from pydantic import ValidationError
from schema import SaleItem


def read_csv(path_to_csv: str) -> list[SaleItem]:
    """Lê um arquivo csv e retorna uma lista de dicionários com cada linha.

    Parameters:
        path_to_csv: Caminho para o arquivo csv a ser lido.

    Returns:
        Uma lista de itens de venda.
    """
    with Path.open(path_to_csv, encoding='utf-8') as file:
        valid_items = []

        for item in csv.DictReader(file):
            try:
                valid_items.append(SaleItem(**item))
            except ValidationError as e:
                print(f'Erro de validação: {e.json()}')

    return valid_items


def group_by_category(
    sales_items: list[SaleItem],
) -> dict[str, list[SaleItem]]:
    """Recebe uma lista de itens de venda e os agrupa por categoria.

    Parameters:
        sales_items: Lista de itens de venda.

    Returns:
        Um dicionário onde as chaves são as categorias e os valores são listas
        de itens de venda naquela categoria.
    """
    items_by_category = {}

    for item in sales_items:
        category = item.Categoria

        if category not in items_by_category:
            items_by_category[category] = []

        items_by_category[category].append(item)

    return items_by_category


def compute_sales_by_category(
    items_by_category: dict[str, list[SaleItem]],
) -> dict[str, float]:
    """Consolida as vendas de produtos por categoria.

    Parameters:
        items_by_category: Dicionário onde as chaves são as categorias e os
        valores são listas de itens de venda naquela categoria.

    Returns:
        Um dicionário onde as chaves são as categorias e os valores são o total
        de vendas naquela categoria.
    """
    sales_by_category = {}

    for category, items in items_by_category.items():
        sales_by_category[category] = sum(
            item.Quantidade * item.Venda for item in items
        )

    return sales_by_category


def run_pipeline(path_to_csv: str) -> None:
    sales_items = read_csv(path_to_csv)
    items_by_category = group_by_category(sales_items)
    sales_by_category = compute_sales_by_category(items_by_category)

    for category, total_sales in sales_by_category.items():
        print(f'{category}: $ {total_sales:.2f}')


if __name__ == '__main__':
    SALES_CSV_PATH = 'vendas.csv'

    run_pipeline(SALES_CSV_PATH)
