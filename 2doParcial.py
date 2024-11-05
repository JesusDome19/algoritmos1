

pokemon_list = [
    {"nombre": "Bulbasaur", "numero": 1, "tipos": "Planta/Veneno"},
    {"nombre": "Charmander", "numero": 4, "tipos": "Fuego"},
    {"nombre": "Squirtle", "numero": 7, "tipos": "Agua"},
    {"nombre": "Chikorita", "numero": 152, "tipos": "Planta"},
    {"nombre": "Cyndaquil", "numero": 155, "tipos": "Fuego"},
    {"nombre": "Totodile", "numero": 158, "tipos": "Agua"},
    {"nombre": "Treecko", "numero": 252, "tipos": "Planta"},
    {"nombre": "Torchic", "numero": 255, "tipos": "Fuego"},
    {"nombre": "Mudkip", "numero": 258, "tipos": "Agua"},
    {"nombre": "Turtwig", "numero": 387, "tipos": "Planta"},
    {"nombre": "Jolteon", "numero": 135, "tipos": "Eléctrico"},
    {"nombre": "Chimchar", "numero": 390, "tipos": "Fuego"},
    {"nombre": "Piplup", "numero": 393, "tipos": "Agua"},
    {"nombre": "Snivy", "numero": 495, "tipos": "Planta"},
    {"nombre": "Lycanroc", "numero": 745, "tipos": "Roca"},
    {"nombre": "Tepig", "numero": 498, "tipos": "Fuego"},
    {"nombre": "Oshawott", "numero": 501, "tipos": "Agua"},
    {"nombre": "Chespin", "numero": 650, "tipos": "Planta"},
    {"nombre": "Fennekin", "numero": 653, "tipos": "Fuego"},
    {"nombre": "Froakie", "numero": 656, "tipos": "Agua"},
    {"nombre": "Rowlet", "numero": 722, "tipos": "Planta/Volador"},
    {"nombre": "Litten", "numero": 725, "tipos": "Fuego"},
    {"nombre": "Popplio", "numero": 728, "tipos": "Agua"},
    {"nombre": "Grookey", "numero": 810, "tipos": "Planta"},
    {"nombre": "Scorbunny", "numero": 813, "tipos": "Fuego"},
    {"nombre": "Sobble", "numero": 816, "tipos": "Agua"}
]

from tree_alv import BinaryTree

tree_nombre = BinaryTree()
tree_numero = BinaryTree()
tree_tipo = BinaryTree()

# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
for pokemon in pokemon_list:
    tree_nombre.insert_node(pokemon["nombre"], pokemon)
    tree_numero.insert_node(pokemon["numero"], pokemon)
    tree_tipo.insert_node(pokemon["tipos"], pokemon)


# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por 
# proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;

Buscado = int(input("Ingresar el numero del pokemon buscado: "))
tree_numero.search_number(Buscado)

bus_aprox = input("\nIngresar las inicales del pokemon buscado: ")
print(f"Lista de los pokemons buscados como {bus_aprox}: ")
tree_nombre.proximity_search_inicial(bus_aprox)


# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
tipos = ["Agua", "Fuego", "Planta", "Eléctrico"]
print("\n Lista de los pokemon que son del tipo agua, fuego, planta y eléctrico")
for tipo in tipos:
    tree_tipo.proximity_search_tipo(tipo)

# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
print("\nListado de pokemon por numero de forma ascendente: ")
tree_numero.inorden()

print("\nListado de pokemon por nombre de forma ascendente: ")
tree_nombre.inorden()

print("\nListado de pokemon por nivel y nombre de forma ascendente: ")
tree_nombre.by_level()

# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
print("\nLos datos de Jolteon, Lycanroc y Tyrantrum")
tree_nombre.proximity_search("Jolteon")
tree_nombre.proximity_search("Tyrantrum")
tree_nombre.proximity_search("Lycanroc")

# f) Determina cuantos Pokémons hay de tipo eléctrico y acero.
resul = tree_tipo.contar_pokemons("Eléctrico")
print(f"\nSe encuantran {resul} pokemons del tipo electrico")

resul = tree_tipo.contar_pokemons("Acero")
print(f"\nSe encuantran {resul} pokemons del tipo Acero")


    