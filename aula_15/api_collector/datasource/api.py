from datetime import datetime
from io import BytesIO

import pandas as pd
import requests
from utils.retry import retry


class APICollector:
    def __init__(self, schema, cloud, base_url='http://127.0.0.1:8000'):
        self._schema = schema
        self._cloud = cloud
        self._buffer = None
        self.base_url = base_url

    def start(self, num_purchases):
        response = self.get_data(num_purchases)
        purchases_list = self.extract_data(response)
        parquet_file = self.convert_to_parquet(purchases_list)

        if self._buffer is not None:
            filename = self.generate_filename()
            print(filename)
            self._cloud.upload_file(parquet_file, filename)
            return True

        return False

    @retry(requests.exceptions.RequestException, tries=5, delay=1, backoff=2)
    def get_data(self, num_purchases):
        if num_purchases > 1:
            response = requests.get(
                f'{self.base_url}/gerar_compras/{num_purchases}',
                timeout=10,
            ).json()
        else:
            response = requests.get(
                f'{self.base_url}/gerar_compra',
                timeout=10,
            ).json()
        return response

    def extract_data(self, response):
        purchases_list: list[self._schema] = []

        for item in response:
            item_dict = {}

            for key, data_type in self._schema.items():
                if isinstance(item.get(key), data_type):
                    item_dict[key] = item[key]
                else:
                    item_dict[key] = None

            purchases_list.append(item_dict)

        return purchases_list

    def convert_to_parquet(self, purchases_list):
        purchases_df = pd.DataFrame(purchases_list)

        self._buffer = BytesIO()

        try:
            with self._buffer as buffer:
                purchases_df.to_parquet(buffer)
                return buffer
        except Exception as e:
            print('Error converting DataFrame to parquet.')
            print(e)
            self._buffer = None

    @staticmethod
    def generate_filename():
        date_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return f'api/api_collected_purchases__{date_time}.parquet'
