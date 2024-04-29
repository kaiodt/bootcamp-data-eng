import time

import schedule
from contracts.schemas import PurchaseSchema
from datasource.api import APICollector
from utils.aws.client import S3Client

schema = PurchaseSchema
cloud = S3Client()


def api_collector(schema, cloud, num_purchases):
    APICollector(schema, cloud).start(num_purchases)
    print('Executado')


schedule.every(1).minutes.do(api_collector, schema, cloud, num_purchases=50)

while True:
    schedule.run_pending()
    time.sleep(1)
