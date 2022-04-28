import csv
import json
import pandas as pd
import random

def dividirPokemons():
    pokemons = pd.read_csv('./Pokemon.csv')
    pokemons.loc[0:400].to_csv('./coach_1_gimnasio.csv', index=False)
    pokemons.loc[0:-1].to_csv('./coach_2_gimnasio.csv', index=False)
    pokemons.loc[401:800].to_csv('./coach_2_gimnasio.csv', index=False)
    # gym_1 = pd.read_csv('./coach_1_gimnasio.csv')
    # gym_2 = pd.read_csv('./coach_2_gimnasio.csv')
    # for j in range(len(gym_1)):
    #     datos_para_media = []
    #     result = gym_1.to_json(orient="split")
    #     parsed = json.loads(result)
    #     pokemon_consult = json.loads(json.dumps(parsed, indent=4))
    #     datos_para_media.append(pokemon_consult["data"][0][4])
    # media = sum(datos_para_media) / len(datos_para_media)
    # encontrado = False
    # index = 1
    # while not encontrado:
    #     for i in range(1, len(pokemons) - 3):
    #         print(i)
    #         pokemon_a_mirar = pokemons.loc[i:i]
    #         result = pokemon_a_mirar.loc[1:1].to_json(orient="split")
    #         parsed = json.loads(result)
    #         pokemon_consult = json.loads(json.dumps(parsed, indent=4))
    #         print(pokemon_consult["data"])
    #         if pokemon_consult["data"][0][4] == media or pokemon_consult["data"][0][4] + index == media or pokemon_consult["data"][0][4] - index == media:
    #             pokemons.loc[i:i].to_csv('./coach_1_gimnasio.csv', index=False)
    #             encontrado = True
    # index += 1

dividirPokemons()

def elegirPokemons():  
    json_stats = open('stats.json')
    stats_entrenadores = json.load(json_stats)
    victorias_1 = stats_entrenadores['entrenador_1']['victorias']
    derrotas_1 = stats_entrenadores['entrenador_1']['derrotas']
    victorias_2 = stats_entrenadores['entrenador_2']['victorias']
    derrotas_2 = stats_entrenadores['entrenador_2']['derrotas']
    raw_entrenador_1 = pd.read_csv(f'./coach_1_gimnasio.csv')
    result = raw_entrenador_1.to_json(orient="split")
    parsed = json.loads(result)
    pokemons_entrenador_1 = json.loads(json.dumps(parsed, indent=4))
    raw_entrenador_2 = pd.read_csv(f'./coach_2_gimnasio.csv')
    result = raw_entrenador_2.to_json(orient="split")
    parsed = json.loads(result)
    pokemons_entrenador_2 = json.loads(json.dumps(parsed, indent=4))
    prioridad = 0
    medias =[]
    pokemons_1 = []
    pokemons_2 = []
    if victorias_1 > victorias_2 and derrotas_1 < derrotas_2:
        prioridad = 2
    elif victorias_1 < victorias_2 and derrotas_1 > derrotas_2:
        prioridad = 1
    else:
        prioridad = random.randint(1, 2)
    for i in range(1, 3):
        with open('./coach_' + str(i) + '_gimnasio.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            numero_pokemons = 0
            for row in csv_reader:
                print(f'\tPokemon {row[0]} de Nombre {row[1]} tiene una media total de {row[4]}.')
                numero_pokemons += 1
            print(f'El entrenador {i} tiene {numero_pokemons} Pokemons disponibles.')
            print('Los entrenadores eligen Pokemons...')
        pokemons_entrenador = pd.read_csv(f'./coach_{i}_gimnasio.csv')
        result = pokemons_entrenador.to_json(orient="split")
        parsed = json.loads(result)
        pokemon_consult = json.loads(json.dumps(parsed, indent=4))
        totales_pokemos = []
        for j in range(numero_pokemons):
            totales_pokemos.append(pokemon_consult["data"][j-1][4])
        media = sum(totales_pokemos) / len(totales_pokemos)
        print(f'La media de los Pokemons del entrenador {i} es {media}.')
        medias.append(float(media))
    print(medias)
    if prioridad == 1:
        while len(pokemons_1) < 3:
            index = random.randint(0, 400)
            if pokemons_entrenador_1['data'][index][4] < medias[1]:
                pokemons_1.append(pokemons_entrenador_1['data'][index])
        while len(pokemons_2) < 3:
            index = random.randint(0, 400)
            if pokemons_entrenador_2['data'][index][4] > medias[0]:
                pokemons_2.append(pokemons_entrenador_2['data'][index])
    elif prioridad == 2:
        while len(pokemons_2) < 3:
            index = random.randint(0, 400)
            if pokemons_entrenador_2['data'][index][4] < medias[0]:
                pokemons_2.append(pokemons_entrenador_2['data'][index])
        while len(pokemons_1) < 3:
            index = random.randint(0, 400)
            if pokemons_entrenador_1['data'][index][4] > medias[1]:
                pokemons_1.append(pokemons_entrenador_1['data'][index])
    print(pokemons_1, pokemons_2)


elegirPokemons()