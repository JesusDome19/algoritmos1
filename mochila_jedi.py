#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u 
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#ayuda de la fuerza” realizar las siguientes actividades:

# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;

#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;

#c. Utilizar un vector para representar la mochila.

mochila = ["regla", "compu", "cartuchera", "carpeta", "sable de luz", "hojas", "libro" ]

def usar_la_fuerza(objetos, pasos = 0):

    if len(objetos) == 0: # Berifico la cantidad de objetos hay en el vecor.
        print("No se encuentran elementos en la mochila.")
        return False, 0

    if objetos[0] == "sable de luz": # Berifico si el sable de luz se encuenta en la posicion inicial.
        return True, pasos + 1 

    else: #La funcion recursiva recorre el vector hasta en contrar el sable de luz y mustra la posicion en caso contrario no devuelve nada.
        return usar_la_fuerza(objetos[1: ], pasos + 1) 

Sable_de_luz, pasos = usar_la_fuerza(mochila) 

if Sable_de_luz == True: # Muestro un mensaje si se encontro el sable de luz o no.
    print(f"Jedi encntro el sable de luz, pero tubo que sacar {pasos} objetos de la mochila antes de hallarlo.")

else:
    print("Jedi no encotro el sable de luz en su mochila, despues de sacar todo los objetos de ella.")
