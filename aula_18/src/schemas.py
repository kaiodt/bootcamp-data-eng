from pydantic import BaseModel


class PokemonSchema(BaseModel):
    name: str
    types: str
