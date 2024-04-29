GenericSchema = dict[str, str | float | int]

PurchaseSchema: GenericSchema = {
    'ean': int,
    'price': float,
    'store': int,
    'datetime': str,
}
