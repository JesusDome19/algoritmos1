# Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
# que contemple las siguientes actividades: 
# a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda tabla la función hash deberá utilizar el ultimo 
# dígito del número del Pokémon como clave y la tercera sera en base a su nivel repartiéndolos en 10 posiciones dentro de la tabla; 
# b. debe utilizar tablas hash abiertas con listas como estructura secundaria;
# c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;
# d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
# e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
# f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
# g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo

def hash_tipo(pokemons):
    return pokemons["tipo"]

def hash_digito(pokemons):
    return pokemons["numero"]%10

def hash_nivel(pokemons):
    return pokemons["nivel"]

def Ingresar_Pokemons(cantidad):
    # Pokemons = {}
    if cantidad > 0:
        for i in range(cantidad):
            Nombre = input("Ingresa nombre del Pokemon: ")
            Numero = int(input("\nIngresar el Numero de Pokemon: "))
            Tipo = input("Ingresar el o los tipo/s del Pokemon: ")
            Nivel = input("Ingrear el Nivel del Pokemon: ")

            Pokemons = { "Nombre": Nombre, "Numero": Numero, "Tipo": Tipo, "Nivel": Nivel}
            
        return Pokemons
    

pokemons=[ 
            {"nombre": "Psyduck", "tipo": "Agua", "nivel": 5, "numero": 54},
            {"nombre": "Snorlax", "tipo": "Normal", "nivel": 7, "numero": 143},
            {"nombre": "Bulbasaur", "tipo": "Planta/Veneno", "nivel": 6, "numero": 1},
            {"nombre": "Geodude", "tipo": "Roca/Tierra", "nivel": 5, "numero": 74},
            {"nombre": "Charmander", "tipo": "Fuego", "nivel": 8, "numero": 4},
            { "nombre": "Machop", "tipo": "Lucha", "nivel": 5, "numero": 67},
            {"nombre": "Eevee", "tipo": "Acero", "nivel": 6,"numero": 133},
            {"nombre": "Meowth", "tipo": "Normal", "nivel": 40, "numero": 52},
            {"nombre": "Squirtle", "tipo": "Agua/Hielo", "nivel": 9, "numero": 7},
            { "nombre": "Pikachu", "tipo": "Electrificado", "nivel": 2, "numero": 25},
            {"nombre": "Jigglypuff", "tipo": "Normal/Hada", "nivel": 130, "numero": 39},
            {"nombre": "Dratini", "tipo": "Dragón", "nivel": 15, "numero": 149}
   ]

table_tipo = {}
table_digito = {}
table_nivel = {}

# pregunta li el usuario quiere ingresar pokemons 
resp = input("Desea ingresar pokemos manualmente? ")
if resp.lower() == "si":
    cantidad = int(input("Ingresar la cantidad de Pokemons: ")) # Pregunta cuanta es la cantidad de pokemos que quiere ingresar 
    I_P = (Ingresar_Pokemons(cantidad))
    pokemons.update(I_P)

for pokemon in pokemons:
    claves = hash_tipo(pokemon).split("/")  # c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;
    for clave in claves:
        if clave not in table_tipo:
            table_tipo[clave] = []
        table_tipo[clave].append(pokemon)
    
for pokemon in pokemons:
    clave = hash_digito(pokemon)
    if clave not in table_digito:
        table_digito[clave] = []
    table_digito[clave].append(pokemon)


for pokemon in pokemons:
    clave = hash_nivel(pokemon)
    if clave not in table_nivel:
        table_nivel[clave] = []
    table_nivel[clave].append(pokemon)

    
    
# e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
if len(table_digito.get(3, [])) > 0:
     print(f"\nPokemons terminados en 3: {table_digito.get(3, [])}")
else:
    print("\nNo se encontro ningun Pokemon que termine en 3")
    
if len(table_digito.get(7, [])) > 0:
    print(f"\nPokemons terminados en 7: {table_digito.get(7, [])}")
else:
    print("\nNo se encontro ningun Pokemon que termine en 7")
    
if len(table_digito.get(9, [])) > 0:
    print(f"\nPokemons terminados en 9: {table_digito.get(9, [])}")
else:
    print("\nNo se encontro ningun Pokemon que termine en 9")
    
# f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
print("\n Los pokemons que son multiplos de 2, 5 y 10 son:")
for nivel in (table_nivel):
    if nivel % 2 == 0 or nivel % 5 == 0 or nivel % 10 == 0:
        print(f"\n  {table_nivel[nivel]}")
        
# g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo
if len(table_tipo.get("Acero", [])) == 0:
    print("No se encontro ningun pokemon del tipo Acero")
else:
    print(table_tipo.get("Acero", []))

if len(table_tipo.get("Fuego", [])) == 0:
    print("No se encontro ningun pokemon del tipo Fuego")
else:
    print(table_tipo.get("Fuego", []))  

if len(table_tipo.get("Electrificado", [])) == 0:
    print("No se encontro ningun pokemon del tipo Electrificado")
else:
    print(table_tipo.get("Electrificado", []))

if len(table_tipo.get("Hielo", [])) == 0:
    print("No se encontro ningun pokemon del tipo Hielo ")
else:   
    print(table_tipo.get("Hielo", []))