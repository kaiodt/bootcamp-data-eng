import pandera as pa
from pandera.dtypes import DateTime
from pandera.typing import Series


class SalesSchema(pa.DataFrameModel):
    Produto: Series[str]
    Categoria: Series[str]
    Quantidade: Series[int] = pa.Field(ge=0)
    Venda: Series[float] = pa.Field(ge=0)
    Data: Series[DateTime]

    class Config:
        coerce = True
        strict = True
