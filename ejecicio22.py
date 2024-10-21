
marvel_Personajes = [
    {"name": "Tony Stark", "superhero_name": "Iron Man", "genero": "M"},
    {"name": "Steve Rogers", "superhero_name": "Capitan America", "genero": "M"},
    {"name": "Natasha Romanoff", "superhero_name": "Black Widow", "genero": "F"},
    {"name": "Bruce Banner", "superhero_name": "Hulk", "genero": "M"},
    {"name": "Thor Odinson", "superhero_name": "Thor", "genero": "M"},
    {"name": "Wanda Maximoff", "superhero_name": "Scarlet Witch", "genero": "F"},
    {"name": "Peter Parker", "superhero_name": "Spider-Man", "genero": "M"},
    {"name": "Carol Danvers", "superhero_name": "Capitana Marvel", "genero": "F"},
    {"name": "T'Challa", "superhero_name": "Black Panther", "genero": "M"},
    {"name": "Scott Lang", "superhero_name": "Ant-Man", "genero": "M"},
    {"name": "Stephen Strange", "superhero_name": "Doctor Strange", "genero": "M"},
    {"name": "Clint Barton", "superhero_name": "Hawkeye", "genero": "M"},
    {"name": "Hope van Dyne", "superhero_name": "The Wasp", "genero": "F"},
    {"name": "Scott Lang", "superhero_name": "Ant-Man", "genero": "M"},
    {"name": "Bucky Barnes", "superhero_name": "Winter Soldier", "genero": "M"},
    {"name": "Sam Wilson", "superhero_name": "Falcon", "genero": "M"},
    {"name": "Gamora", "superhero_name": "Gamora", "genero": "F"},
    {"name": "Peter Quill", "superhero_name": "Star-Lord", "genero": "M"},
    {"name": "Gwen Stacy", "superhero_name": "Spider-Gwen", "genero": "F"},
    {"name": "Jessica Jones", "superhero_name": "Jessica Jones", "genero": "F"},
    {"name": "Matt Murdock", "superhero_name": "Daredevil", "genero": "M"}
]

from cola import Queue

cola = Queue()
cola_aux = Queue()
persFemeninos = Queue()
persMasculinos = Queue()

for personaje in marvel_Personajes:
    cola.arrive(personaje)

#a.determinar el nombre del personaje de la superhéroe Capitana Marvel;
capitana = None
SL = None #abreviatura de Scott Lang
while (cola.size() > 0):
    dato = cola.attention()
    if dato["superhero_name"] == "Capitana Marvel":
        capitana = dato
    #compara para ver cuales son los superhéroes femeninos;
    if dato["genero"] == "F":
        persFemeninos.arrive(dato) 
    #compara para ver cuales son los personajes masculinos;
    if dato["genero"] == "M":
        persMasculinos.arrive(dato)   

    if dato["name"] == "Scott Lang":
        SL = dato["superhero_name"]

    cola_aux.arrive(dato)

if capitana is not None:
    print(f"El nombre de la Capitana Marvel es {capitana["name"]}")
else:
    print("La capitana Marvel no se encuenra el la cola")

#b.mostrar los nombre de los superhéroes femeninos;

print("\nNombre de los personajes femeninos de Marvel que estan en la cola son: ")      
while (persFemeninos.size() > 0):
    nombresF = persFemeninos.attention()
    print(f" {nombresF["name"]}")


#c.mostrar los nombres de los personajes masculinos;
print("\nNonbre de los personajes masculinos de Marvel que estan en la cola son: ")
while (persMasculinos.size() > 0):
    nombresM = persMasculinos.attention()
    print(f" {nombresM["name"]}")

#d.determinar el nombre del superhéroe del personaje Scott Lang;
if SL is not None:
    print(f"\nEl nombre del super heroe Scott Lang es {SL}")
else:
    print("No se encunatra el personaje Scott Lang")

#e.mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
print("\nLos personajes y super heroes que empiezan con 'S' son: \n")
while (cola_aux.size() > 0):
    dato = cola_aux.attention()
    if dato["name"].startswith("S") or dato["superhero_name"].startswith("S"):
        print(f" {dato}")

    cola.arrive(dato)

#f.determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
while (cola.size() > 0):
    dato = cola.attention()
    if dato["name"] in "Carol Danvers":
        print(f"\nCarol Danvers se encuentra en la cola, su nombre de super heroe es {dato["superhero_name"]}")