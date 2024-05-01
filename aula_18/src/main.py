import time
from random import randint

import schedule
from controller import add_pokemon_to_db, get_pokemon_info


def get_and_save_new_pokemon():
    # Gerar um número de Pokémon aleatório
    pokemon_id = randint(1, 350)

    # Obter informações sobre o Pokémon a partir da API
    pokemon_info = get_pokemon_info(pokemon_id=pokemon_id)

    if pokemon_info:
        # Salvar no banco de dados
        print(f'Salvando Pokémon {pokemon_info.name} no banco de dados...')
        add_pokemon_to_db(pokemon_info)


schedule.every(10).seconds.do(get_and_save_new_pokemon)

while True:
    schedule.run_pending()
    time.sleep(1)
