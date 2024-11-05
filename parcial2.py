# Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
# algoritmos necesarios para resolver las siguientes tareas:
# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se
# relacionan;
# b) hallar el árbol de expansión minino y determinar si contiene a Yoda
# c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son. 
# d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.

# Lista de personajes
# Lista de personajes
personajes = [
    {"nombre": "Luke Skywalker"},
    {"nombre": "Darth Vader"},
    {"nombre": "Yoda"},
    {"nombre": "Boba Fett"},
    {"nombre": "C-3PO"},
    {"nombre": "Leia"},
    {"nombre": "Rey"},
    {"nombre": "Kylo Ren"},
    {"nombre": "Chewbacca"},
    {"nombre": "Han Solo"},
    {"nombre": "R2-D2"},
    {"nombre": "BB-8"}
]

# Lista de relaciones (aristas) con los episodios en los que aparecieron juntos
relaciones = [
    {"personaje1": "Luke Skywalker", "personaje2": "Darth Vader", "episodios_juntos": 2},
    {"personaje1": "Luke Skywalker", "personaje2": "Yoda", "episodios_juntos": 2},
    {"personaje1": "Luke Skywalker", "personaje2": "Leia", "episodios_juntos": 4},
    {"personaje1": "Leia", "personaje2": "Han Solo", "episodios_juntos": 3},
    {"personaje1": "Leia", "personaje2": "C-3PO", "episodios_juntos": 5},
    {"personaje1": "Leia", "personaje2": "Chewbacca", "episodios_juntos": 3},
    {"personaje1": "Chewbacca", "personaje2": "Han Solo", "episodios_juntos": 3},
    {"personaje1": "Han Solo", "personaje2": "R2-D2", "episodios_juntos": 2},
    {"personaje1": "Yoda", "personaje2": "Luke Skywalker", "episodios_juntos": 2},
    {"personaje1": "R2-D2", "personaje2": "Luke Skywalker", "episodios_juntos": 4},
    {"personaje1": "C-3PO", "personaje2": "R2-D2", "episodios_juntos": 6},
    {"personaje1": "Rey", "personaje2": "BB-8", "episodios_juntos": 2},
    {"personaje1": "Rey", "personaje2": "Kylo Ren", "episodios_juntos": 2},
    {"personaje1": "Rey", "personaje2": "Leia", "episodios_juntos": 1},
    {"personaje1": "Kylo Ren", "personaje2": "Han Solo", "episodios_juntos": 1},
]

from grafo import Graph

grafo = Graph()

# Insertamos los personajes como vértices
for personaje in personajes:
    grafo.insert_vertice(personaje["nombre"])

# Insertamos las relaciones como aristas
for relacion in relaciones:
    grafo.insert_arista(relacion["personaje1"], relacion["personaje2"], relacion["episodios_juntos"])

# Nuestro como quedo el grafo
grafo.show_graph()

# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
arbol_expansion = grafo.kruskal("")

contiene_yoda = False
for arista in arbol_expansion:
    if "Yoda" in arista:
        contiene_yoda = True
        break
if contiene_yoda:
    print("\nEl árbol de expansión mínimo contiene a Yoda.")
else:
    print("\nEl árbol de expansión mínimo no contiene a Yoda.")



# c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son.
def max_episodios(grafo):
    max_episodios = 0
    personajes = ("", "")
    
    for nodo in grafo.elements:
        for arista in nodo['aristas']:
            if arista['peso'] > max_episodios:
                max_episodios = arista['peso']
                personajes = (nodo['value'], arista['value'])
    
    return max_episodios, personajes

max_episodios_valor, personajes = max_episodios(grafo)
print(f"\nEl máximo de episodios compartidos es {max_episodios_valor} entre {personajes[0]} y {personajes[1]}.")


