from pydantic import BaseModel, PositiveFloat, PositiveInt


class SaleItem(BaseModel):
    Produto: str
    Categoria: str
    Quantidade: PositiveInt
    Venda: PositiveFloat
