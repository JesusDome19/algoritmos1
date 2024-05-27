from pila import stack
from peliculas import personaje

pila_marvel = stack()
pila_aux = stack()
marvel = stack()

#lista de los personajes de Marvel Cinematic Universe (MCU)
personajes_marvel = [
    personaje("Iron Man", 10),
    personaje("Capitan America", 9),
    personaje("Thor", 8),
    personaje("Black Widow", 7), 
    personaje("Hulk", 6), 
    personaje("Spider-Man", 5),
    personaje("Black Panther", 4), 
    personaje("Doctor Strange", 3), 
    personaje("Ant-Man", 3),
    personaje("Hawkeye", 3),
    personaje("Scarlet witch", 3),
    personaje("Vision", 3),
    personaje("Falcon", 3),
    personaje("winter Soldier", 3),
    personaje("war Machine", 3),
    personaje("Groot", 3),
    personaje("Rocket Raccoon", 3),
    personaje("Drax the Destroyer",  3),
    personaje("Gamora", 3),
    personaje("Nebula", 3),
    personaje("Stra Lord", 3),
    personaje("Mantis", 3),
    personaje("Okoye", 3),
    personaje("Shuri", 3),
    personaje("Wong", 3),
    personaje("Nick Fury", 10),
    personaje("Agent Coulson", 2),
    personaje("Loki", 6),
    personaje("Thanos", 5),
]

contador = 0
pos_rocket = 0
pos_groot = 0
Black_Widow = 0

for protagonista in personajes_marvel: 
    pila_marvel.push(protagonista)
    pila_aux.push(protagonista)



#a)determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
while (pila_marvel.size() > 0):
    dato = pila_marvel.pop().nombre
    contador += 1

    if dato == "Rocket Raccoon":
        pos_rocket = contador
    
    elif dato == "Groot":
        pos_groot = contador

    
    marvel.push(dato)



#b)determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
while (pila_aux.size() > 0):
    dato = pila_aux.pop()

    if dato.cant_peli >= 5:
        pila_marvel.push(dato)


#d)mostrar todos los personajes cuyos nombre empiezan con C, D y G.
while (marvel.size() > 0):
    dato = marvel.pop()

    if dato[0].lower() in ['c', 'd', 'g']:  # Verificar si el nombre comienza con 'c', 'd' o 'g'
       pila_aux.push(dato) 

print(f"a) Rocket Raccoon se encuentra en la posicion {pos_rocket} y Groot en la posicion {pos_groot}")

print(f"b) Personajes que aparecen en mas de cinco peliculas: ")
while (pila_marvel.size() > 0):
    datos = pila_marvel.pop()
    print(" ", datos)

    if datos.nombre == "Black Widow": #c)determinar en cuantas películas participo la Viuda Negra (Black Widow);
        Black_Widow = datos.cant_peli

print(f"c) Black Widow participo en {Black_Widow} peliculas")

print("d)Personajes que su nombre empiza con las letras 'C, D o G'")
while (pila_aux.size() > 0):
    print(" ", pila_aux.pop())