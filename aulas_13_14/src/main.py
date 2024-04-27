import time

import schedule
from source_classes.CSVSource import CSVSource
from source_classes.JSONSource import JSONSource
from source_classes.TXTSource import TXTSource


def update_data(sources: list) -> None:
    for source in sources:
        source.update_data()


sources = [CSVSource(), TXTSource(), JSONSource()]

schedule.every(10).seconds.do(update_data, sources=sources)

while True:
    schedule.run_pending()
    time.sleep(1)
