import csv
import random

from faker import Faker

fake = Faker()


def generate_products(n_products: int) -> list[tuple[str, str, float]]:
    """Gera dados fictícios de determinado número de produtos."""
    products = []
    for _ in range(n_products):
        ean = fake.ean(length=13)
        product_name = f'{fake.word()} {fake.word()}'.title()
        price = round(random.uniform(10.0, 1000.0), 2)
        products.append((ean, product_name, price))
    return products


def save_products(
        products: list[tuple[str, str, float]],
        filename: str = 'data/products.csv',
    ) -> None:
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['EAN', 'Product Name', 'Price'])  # Header
        writer.writerows(products)  # Dados dos produtos


if __name__ == '__main__':
    save_products(
        products=generate_products(200),
        filename='product_data/products.csv',
    )
