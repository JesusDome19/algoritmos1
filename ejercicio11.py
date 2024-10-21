#Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
#de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
#a.mostrar los personajes del planeta Alderaan, Endor y Tatooine
#b.indicar el plantea natal de Luke Skywalker y Han Solo
#c. insertar un nuevo personaje antes del maestro Yoda
#d.eliminar el personaje ubicado después de Jar Jar Binks

star_wars_personajes = [
    {"name": "Luke Skywalker", "planet": "Tatooine"},
    {"name": "Leia Organa", "planet": "Alderaan"},
    {"name": "Bail Organa", "planet": "Alderaan"},
    {"name": "Breha Organa", "planet": "Alderaan"},
    {"name": "Han Solo", "planet": "Corellia"},
    {"name": "Darth Vader", "planet": "Tatooine"},
    {"name": "Yoda", "planet": "Dagobah"},
    {"name": "Obi-Wan Kenobi", "planet": "Stewjon"},
    {"name": "Palpatine", "planet": "Naboo"},
    {"name": "Padmé Amidala", "planet": "Naboo"},
    {"name": "Chewbacca", "planet": "Kashyyyk"},
    {"name": "Lando Calrissian", "planet": "Socorro"},
    {"name": "Boba Fett", "planet": "Kamino"},
    {"name": "Jar Jar Binks", "planet": "Naboo"},
    {"name": "Rey", "planet": "Jakku"}, #se tiene que eliminar
    {"name": "Finn", "planet": "Unknown (raised on First Order territory)"},
    {"name": "Kylo Ren", "planet": "Chandrila"},
    {"name": "Ahsoka Tano", "planet": "Shili"},
    {"name": "Wicket W. Warrick", "planet": "Endor"},
    {"name": "Chief Chirpa", "planet": "Endor"},
    {"name": "Logray", "planet": "Endor"}
]
from cola import Queue

cola = Queue()
cola_aux = Queue()

print("Cola original: ")
for personaje in star_wars_personajes:
    print(personaje)
    cola.arrive(personaje)

#a.mostrar los personajes del planeta Alderaan, Endor y Tatooine
print("\nlos personajes del planta 'Alderaan', 'Endor', 'Tatooine' son: ")
while (cola.size() > 0):
    dato = cola.attention()
    if dato["planet"] in ("Alderaan", "Endor", "Tatooine"):
        print(f" {dato}") 
    cola_aux.arrive(dato)

#b.indicar el plantea natal de Luke Skywalker y Han Solo
while (cola_aux.size() > 0):
    dato = cola_aux.attention()
    if dato["name"] in ("Luke Skywalker", "Han Solo"):
        print(f"\nEl planeta natal de {dato["name"]} es {dato["planet"]}")
    cola.arrive(dato)


#c. insertar un nuevo personaje antes del maestro Yoda
new_character = {"name": "Qui-Gon Jinn", "planet": "Coruscant"}
while (cola.size() > 0):
    dato = cola.attention()
    if dato["name"] == "Yoda":
        cola_aux.arrive(new_character)
        print(f"\nEl personaje nuevo que esta despues de 'Yoda' es {new_character} ")
    cola_aux.arrive(dato)

#d.eliminar el personaje ubicado después de Jar Jar Binks
while (cola_aux.size() > 0):
    dato = cola_aux.attention()
    if dato["name"] == "Jar Jar Binks":
        eliminar = cola_aux.attention()
        print(f"El personaje elimindo ubicado despue de 'Jar Jar Binks' es {eliminar}")
    cola.arrive(dato)
   
print("\nCola final: ")
while (cola.size() > 0):
    print(cola.attention())