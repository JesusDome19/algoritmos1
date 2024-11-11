# Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, 
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan 
# para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para 
# determinar cuántos metros de cable de red se necesitan para conectar el router con el 
# Smart Tv

ambientes = [
    {
        "ambiente": "cocina",
        "conexiones": [
            {"ambiente": "comedor", "distancia": 3},
            {"ambiente": "patio", "distancia": 5},
            {"ambiente": "baño uno", "distancia": 7}
        ]
    },
    {
        "ambiente": "comedor",
        "conexiones": [
            {"ambiente": "cocina", "distancia": 3},
            {"ambiente": "sala de estar", "distancia": 4},
            {"ambiente": "terraza", "distancia": 6}
        ]
    },
    {
        "ambiente": "cochera",
        "conexiones": [
            {"ambiente": "patio", "distancia": 10},
            {"ambiente": "quincho", "distancia": 8}
        ]
    },
    {
        "ambiente": "quincho",
        "conexiones": [
            {"ambiente": "patio", "distancia": 6},
            {"ambiente": "terraza", "distancia": 12}
        ]
    },
    {
        "ambiente": "baño uno",
        "conexiones": [
            {"ambiente": "cocina", "distancia": 7},
            {"ambiente": "habitación uno", "distancia": 4}
        ]
    },
    {
        "ambiente": "baño dos",
        "conexiones": [
            {"ambiente": "habitación dos", "distancia": 3},
            {"ambiente": "sala de estar", "distancia": 5}
        ]
    },
    {
        "ambiente": "habitación uno",
        "conexiones": [
            {"ambiente": "baño uno", "distancia": 4},
            {"ambiente": "sala de estar", "distancia": 6}
        ]
    },
    {
        "ambiente": "habitación dos",
        "conexiones": [
            {"ambiente": "baño dos", "distancia": 3},
            {"ambiente": "sala de estar", "distancia": 7}
        ]
    },
    {
        "ambiente": "sala de estar",
        "conexiones": [
            {"ambiente": "comedor", "distancia": 4},
            {"ambiente": "habitación uno", "distancia": 6},
            {"ambiente": "cochera", "distancia": 8},
            {"ambiente": "habitación dos", "distancia": 7},
            {"ambiente": "baño dos", "distancia": 5}
        ]
    },
    {
        "ambiente": "terraza",
        "conexiones": [
            {"ambiente": "comedor", "distancia": 6},
            {"ambiente": "quincho", "distancia": 12},
            {"ambiente": "patio", "distancia": 9}
        ]
    },
    {
        "ambiente": "patio",
        "conexiones": [
            {"ambiente": "cocina", "distancia": 5},
            {"ambiente": "terraza", "distancia": 9},
            {"ambiente": "baño dos", "distancia": 8},
            {"ambiente": "cochera", "distancia": 10},
            {"ambiente": "quincho", "distancia": 6}
        ]
    }
]

from grafo import Graph

grafo = Graph(dirigido=False)

for ambiente in ambientes:
    grafo.insert_vertice(ambiente["ambiente"])
    for conexion in ambiente["conexiones"]: 
        grafo.insert_arista(ambiente["ambiente"], conexion["ambiente"], conexion["distancia"])
    
arbol_expansion = grafo.kruskal("")
cant_cable = 0
for arista in arbol_expansion:
    for dato in arista:
        if dato.isdigit(): 
            cant_cable = cant_cable + int(dato)

print(f"\n Se necesitan {cant_cable} metros de cable para conectar todas la abitaciones de la casa. " )

camino_minimo = grafo.dijkstra("habitación uno")
while  camino_minimo.size() > 0:
    nodo = camino_minimo.pop()
    if nodo[1][0] in "sala de estar":
        camino = nodo

print(f"\n El camino mas corto desde la Habitacion 1 a la Sala de estar es nodo {camino}")

print(f"\n Se necesitan {camino[0]} metros de cable de red para conectar el router con el Smart Tv")

# grafo.show_graph()
