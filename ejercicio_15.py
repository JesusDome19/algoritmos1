from listas import show_list_list, by_name, search, by_torneos
from random import choice

entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60
    }
]

pokemons = [
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Tyrantrum",
        "nivel": 70,  
        "tipo": "Roca",
        "subtipo": "Dragón"
    },
     {
        "nombre": "Terrakion",
        "nivel": 65,  
        "tipo": "Roca",
        "subtipo": "Lucha"
    },
     {
        "nombre": "Wingull",
        "nivel": 15, 
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Pikachu",
        "nivel": 20,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": "Planta"
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Dragonite",
        "nivel": 55,
        "tipo": "Dragón",
        "subtipo": "Volador"
    },
    {
        "nombre": "Aerodactyl",
        "nivel": 52,
        "tipo": "Roca",
        "subtipo": "Volador"
    }
]

# Función para obtener entrenadores con Pokémons de tipos fuego y planta o agua y volador
def entrenadores_pockemon(list_entrenadores):
    entrenadores_con_pokemon = []
    for entrenador in list_entrenadores:
        for pokemon in entrenador['pokemons']:
            if (pokemon['tipo'] == 'Fuego') and (pokemon['subtipo'] == 'Planta') or \
                (pokemon['tipo'] == 'Agua') and (pokemon['subtipo'] == 'Volador'):
                entrenadores_con_pokemon.append(entrenador)
                break
    return entrenadores_con_pokemon

#  calcula el promedio de nivel de los Pokémons del entrenador ingresado anteriormente;
def pokemon_nivel(ListEntrenadores, Buscado):
    posbuscado = search(ListEntrenadores, 'nombre', Buscado.capitalize())
    NivelTotal = 0
    cont = 0
    
    for pokemon in ListEntrenadores[posbuscado]['pokemons']:
        cont += 1
        NivelTotal += pokemon['nivel']
        
    if cont != 0:
        promedio_nivel = (NivelTotal / cont)
        print(f"El nivel de los pokemones del entrenador {ListEntrenadores[posbuscado]['nombre']} es de {promedio_nivel}")
        
    else:
        print(f"El entrenador {ListEntrenadores[posbuscado]['nombre']} no tiene pokemons")
    return promedio_nivel

# busca los entrenadores tienen a un determinado Pokémon;
def pokemon_varios_entrenadores(ListEntrenadores, Buscado):
    print(f"Entrenadores que tiene en su equipo a {Buscado.capitalize()}")
    for entrenador in ListEntrenadores:
        for pokemon in entrenador['pokemons']:
            if pokemon['nombre'] == Buscado.capitalize():
                print(entrenador)

#Busca los pokemons repetidos de un entrenador
def pokemons_repetidos(ListEntrenadores):
    for entrenador in ListEntrenadores:
        repetidos = []
        for index, pokemon in enumerate(entrenador['pokemons']):
            for NextPokemon in range(index+1, len(entrenador['pokemons'])):
                if pokemon['nombre'] == entrenador['pokemons'][NextPokemon]['nombre']:
                    repetidos.append(pokemon['nombre'])
        
        if len(repetidos) > 0:
            print(f"El entrenador {entrenador['nombre']} tiene repetidos los pokemones  {repetidos}")
            
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingul
def Buscar_Pokemon(ListEntrenadores):
    E_de_T_T_W = []
    for Entrenador in ListEntrenadores:
        for Pokemon in Entrenador['pokemons']:
            if Pokemon['nombre'].startswith(("Tyrantrum", "Terrakion", "Wingul")):
                E_de_T_T_W.append(Entrenador)
    return E_de_T_T_W


def Buscar_Entrenador_Pokemon(ListEntrenadores, E_buscado, P_buscado):
    E_B_Pos = search(ListEntrenadores, "nombre", E_buscado.capitalize())
    buscados = []
    
    for pokemon_y in ListEntrenadores[E_B_Pos]['pokemons']:
        if pokemon_y['nombre'] == P_buscado.capitalize():
            buscados.append(ListEntrenadores[E_B_Pos])
    
    if len(buscados) == 0:
        print(f"El entrenador {E_buscado} no tiene al pokemon {P_buscado}") 
        
    return buscados  
    
# a. obtener la cantidad de Pokémons de un determinado entrenador;
names = ["Ash Ketchum", "Goh", "Leon", "Chloe", "Raihan"]

lista_entrenadores = []

for entrenador in entrenadores:
    entrenador.update({'pokemons': []})
    lista_entrenadores.append(entrenador)


for pokemon in pokemons:
    pos = search(lista_entrenadores, 'nombre', choice(names))
    if pos is not None:
        lista_entrenadores[pos]['pokemons'].append(pokemon)
    else:
        print('no existe el entrenador')
    
lista_entrenadores.sort(key=by_name)
show_list_list('Entrenadores', 'Pokemons', lista_entrenadores)

# listar los entrenadores que hayan ganado más de tres torneos;
lista_entrenadores.sort(key=by_torneos)
for entrenador in lista_entrenadores:
    if entrenador['torneos_ganados'] >= 3:
        print(f"{entrenador['nombre']}, \n torneos ganados: {entrenador['torneos_ganados']}")
        

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;

# EntrenadorMasGanador = lista_entrenadores[0]

# for entrenador in lista_entrenadores[1:]: 
#     if EntrenadorMasGanador['torneos_ganados'] < entrenador['torneos_ganados']:
#         EntrenadorMasGanador = entrenador
        
# PokemoMayorNivel = EntrenadorMasGanador['pokemons'][0]

# for pokemon in EntrenadorMasGanador['pokemons'][1:]:
#     if pokemon['nivel'] > PokemoMayorNivel['nivel']:
#         PokemoMayorNivel = pokemon

# print(f"El entrenador que gano mas torneos es {EntrenadorMasGanador} \n \nEl pokemon con mayor nivel es {PokemoMayorNivel}")

# d. mostrar todos los datos de un entrenador y sus Pokémos;
pos = search(lista_entrenadores, 'nombre', 'Ash Ketchum')
print(f"\n Ash Ketchum y de sus pokemones: \n{lista_entrenadores[pos]}")

# c. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;

for entrenador in lista_entrenadores:
    BattallasTotal = (entrenador['batallas_perdidas'] + entrenador['batallas_ganadas'])
    porcentaje_batallas_ganadas = (entrenador['batallas_ganadas'] / BattallasTotal ) * 100
    
    if porcentaje_batallas_ganadas > 79:
        print(f"\n{entrenador['nombre']} gano el {porcentaje_batallas_ganadas}% de sus batallas")

        
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua y volador (tipo y subtipo);
# EntrenadoresPokemon = entrenadores_pockemon(lista_entrenadores)
# if EntrenadoresPokemon:
#     print("\nEntrenadores con pokeoes de tipo fuego y planta o agua y volador")
#     for Entrenador in EntrenadoresPokemon:
#         print(Entrenador)
# else:
#     print("No se encontró ningún entrenador con pokemon de tipo fuego y planta, o agua y volador.")
    
    
    
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# EntrenadorBuscado = input("Ingresar el entrenador a buscar para calcular el promedio del nivel de sus pokemons: \n")
# NivelPromedio = pokemon_nivel(lista_entrenadores, EntrenadorBuscado)


# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# PokemonBuscado = input("Ingresar el pokemon que deseas saber cuantos entrenador lo tienen: \n")
# EntendoresConPokemon = pokemon_varios_entrenadores(lista_entrenadores, PokemonBuscado)


# i. mostrar los entrenadores que tienen Pokémons repetidos;
PokemonsRepetidos = pokemons_repetidos(lista_entrenadores)

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingul
EntredoresTieneUnPokemon = Buscar_Pokemon(lista_entrenadores)
if EntredoresTieneUnPokemon is not None:
    print("Los entrenadors que tiene a 'Tyrantrum, Terrakion o Wingul' son: ")
    for Dt_pokemon in EntredoresTieneUnPokemon:
        print(f"\n {Dt_pokemon}")
        
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados; 
# además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;

x = input("\nIngresar el nombre del entrenador a busacar: ")
y = input("\nIngresar el nombre del pokemon a busacar: ")
  
PokemonEntrnadorBuscado = Buscar_Entrenador_Pokemon(lista_entrenadores, x, y)
print(f"los datos del entrenador {x}: nombre: {PokemonEntrnadorBuscado[0]['nombre']}, torneos_ganados: {PokemonEntrnadorBuscado[0]['torneos_ganados']}, batallas_perdidas: {PokemonEntrnadorBuscado[0]['batallas_perdidas']}, batallas_ganadas: {PokemonEntrnadorBuscado[0]['batallas_ganadas']} ")
for pokemon_y in PokemonEntrnadorBuscado[0]['pokemons']:
     if pokemon_y['nombre'] == y.capitalize():
        print(f"los datos del pokemon {y} {pokemon_y}")
        
