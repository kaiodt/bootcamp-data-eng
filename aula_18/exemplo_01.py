import requests


def get_pokemon_info(
        *,
        pokemon_id: int | None = None,
        pokemon_name: str | None = None,
    ) -> str | None:

    # URL do endpoint de Pokémons da API
    base_url = 'https://pokeapi.co/api/v2/pokemon'

    # Terminando de montar o endpoint com o nome ou id do Pokémon
    if pokemon_id is not None:
        url = f'{base_url}/{pokemon_id}'
    elif pokemon_name is not None:
        url = f'{base_url}/{pokemon_name}'
    else:
        msg = 'Forneça o ID ou o nome do Pokémon desejado.'
        raise ValueError(msg)

    # Fazendo a requisição na API
    response = requests.get(url, timeout=10)

    # Selecionando as informações desejadas contidas na resposta
    if response.status_code == 200:
        data = response.json()

        name = data['name'].title()
        types = ', '.join([
            type_info['type']['name'].title()
            for type_info in data['types']
        ])

        return f'{name.title()}: {", ".join(types)}'

    print(f'Erro ao obter informações do Pokémon: {response.status_code}')
    return None


# Exemplos de uso
print(get_pokemon_info(pokemon_name='pikachu'))  # Pikachu: Electric
print(get_pokemon_info(pokemon_id=6))            # Charizard: Fire, Flying
