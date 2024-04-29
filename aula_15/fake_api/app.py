import random

import pandas as pd
from faker import Faker
from fastapi import FastAPI

app = FastAPI(debug=True)
fake = Faker()

input_filename = 'product_data/products.csv'
df = pd.read_csv(input_filename)


@app.get('/gerar_compra')
async def gerar_compra():
    product = df.sample(1).iloc[0]
    return [{
        'client': fake.name(),
        'creditcard': fake.credit_card_provider(),
        'product_name': product['Product Name'],
        'ean': int(product['EAN']),
        'price': round(product['Price'] * 1.1, 2),
        'client_position': fake.location_on_land(),
        'store': random.randint(1, 10),
        'datetime': fake.iso8601(),
    }]


@app.get('/gerar_compras/{numero_registros}')
async def gerar_compras(numero_registros: int) -> list[dict] | dict:
    if numero_registros < 1:
        return {'error': 'Número de registros deve ser no mínimo 1.'}

    compras = []
    for _ in range(numero_registros):
        product = df.sample(1).iloc[0]
        compras.append({
            'client': fake.name(),
            'creditcard': fake.credit_card_provider(),
            'product_name': product['Product Name'],
            'ean': int(product['EAN']),
            'price': round(product['Price'] * 1.1, 2),
            'client_position': fake.location_on_land(),
            'store': random.randint(1, 10),
            'datetime': fake.iso8601(),
        })

    return compras
