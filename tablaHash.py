class Pokemon:
    def __init__(self, numero, nombre, tipos, nivel):
        self.numero = numero
        self.nombre = nombre
        self.tipos = tipos
        self.nivel = nivel

    def __repr__(self):
        return f"{self.nombre} (#{self.numero}, Nivel: {self.nivel}, Tipos: {self.tipos})"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_tipo(self, tipo):
        return hash(tipo) % self.size

    def hash_numero(self, numero):
        return numero % 10

    def hash_nivel(self, nivel):
        return nivel % 10

    def add(self, key, value, hash_function):
        index = hash_function(key)
        self.table[index].append(value)

    def get_all(self, hash_function=None, condition=None):
        result = []
        for bucket in self.table:
            for item in bucket:
                if condition is None or condition(item):
                    result.append(item)
        return result

# Crear las tres tablas hash
tabla_tipos = HashTable(10)  # Tamaño arbitrario
tabla_numeros = HashTable(10)  # Tamaño fijo de 10
tabla_niveles = HashTable(10)  # Tamaño fijo de 10

def cargar_pokemon(numero, nombre, tipos, nivel):
    pokemon = Pokemon(numero, nombre, tipos, nivel)
    # Añadir a la tabla de tipos
    for tipo in tipos:
        tabla_tipos.add(tipo, pokemon, tabla_tipos.hash_tipo)
    # Añadir a la tabla de números
    tabla_numeros.add(numero, pokemon, tabla_numeros.hash_numero)
    # Añadir a la tabla de niveles
    tabla_niveles.add(nivel, pokemon, tabla_niveles.hash_nivel)

# Ejemplo de carga de Pokémons
cargar_pokemon(123, "Charmander", ["Fuego"], 15)
cargar_pokemon(234, "Squirtle", ["Agua"], 10)
cargar_pokemon(347, "Bulbasaur", ["Planta", "Veneno"], 20)
cargar_pokemon(679, "Pikachu", ["Eléctrico"], 5)
cargar_pokemon(879, "Steelix", ["Acero", "Tierra"], 35)

# Mostrar Pokémons cuyos números terminan en 3, 7 y 9
pokemons_numeros_terminan_3_7_9 = []
for digito in [3, 7, 9]:
    pokemons_numeros_terminan_3_7_9.extend(tabla_numeros.get_all(
        condition=lambda p: p.numero % 10 == digito
    ))
print("Pokémons cuyos números terminan en 3, 7 y 9:")
for p in pokemons_numeros_terminan_3_7_9:
    print(p)

# Mostrar Pokémons cuyos niveles son múltiplos de 2, 5 y 10
pokemons_niveles_multiplos_2_5_10 = []
for multiple in [2, 5, 10]:
    pokemons_niveles_multiplos_2_5_10.extend(tabla_niveles.get_all(
        condition=lambda p: p.nivel % multiple == 0
    ))
print("\nPokémons cuyos niveles son múltiplos de 2, 5 y 10:")
for p in pokemons_niveles_multiplos_2_5_10:
    print(p)

# Mostrar Pokémons de tipo Acero, Fuego, Eléctrico, Hielo
tipos_interes = ["Acero", "Fuego", "Eléctrico", "Hielo"]
pokemons_tipos_interes = []
for tipo in tipos_interes:
    pokemons_tipos_interes.extend(tabla_tipos.get_all(
        condition=lambda p, tipo=tipo: tipo in p.tipos
    ))
print("\nPokémons de tipo Acero, Fuego, Eléctrico, Hielo:")
for p in pokemons_tipos_interes:
    print(p)
