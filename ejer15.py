# se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales del mundo, 
# para lo cual se deben tener en cuenta las siguientes actividades:
# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de 
# uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar 
# la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.


# Lista de maravillas arquitectónicas y naturales

maravillas = [
    # Maravillas arquitectónicas modernas
    {
        "nombre": "Gran Muralla China",
        "país": "China",
        "tipo": "arquitectónica",
        "distancias": [
            {"Maravilla": "Petra", "dist": 7000},  # distancia en km
            {"Maravilla": "Cristo Redentor", "dist": 19000},
            {"Maravilla": "Machu Picchu", "dist": 18000},
            {"Maravilla": "Chichén Itzá", "dist": 12000},
            {"Maravilla": "Coliseo de Roma", "dist": 8000},
            {"Maravilla": "Taj Mahal", "dist": 6000}
        ]
    },
    {
        "nombre": "Petra",
        "país": "Jordania",
        "tipo": "arquitectónica",
        "distancias": [
            {"Maravilla": "Gran Muralla China", "dist": 7000},
            {"Maravilla": "Cristo Redentor", "dist": 13000},
            {"Maravilla": "Machu Picchu", "dist": 14000},
            {"Maravilla": "Chichén Itzá", "dist": 10000},
            {"Maravilla": "Coliseo de Roma", "dist": 3000},
            {"Maravilla": "Taj Mahal", "dist": 4000}
        ]
    },
    {
        "nombre": "Cristo Redentor",
        "país": "Brasil",
        "tipo": "arquitectónica",
        "distancias": [
            {"Maravilla": "Gran Muralla China", "dist": 19000},
            {"Maravilla": "Petra", "dist": 13000},
            {"Maravilla": "Machu Picchu", "dist": 3600},
            {"Maravilla": "Chichén Itzá", "dist": 7000},
            {"Maravilla": "Coliseo de Roma", "dist": 9600},
            {"Maravilla": "Taj Mahal", "dist": 15000}
        ]
    },
    {
        "nombre": "Machu Picchu",
        "país": "Perú",
        "tipo": "arquitectónica",
        "distancias": [
            {"Maravilla": "Gran Muralla China", "dist": 18000},
            {"Maravilla": "Petra", "dist": 14000},
            {"Maravilla": "Cristo Redentor", "dist": 3600},
            {"Maravilla": "Chichén Itzá", "dist": 6000},
            {"Maravilla": "Coliseo de Roma", "dist": 10500},
            {"Maravilla": "Taj Mahal", "dist": 15000}
        ]
    },
    {
        "nombre": "Chichén Itzá",
        "país": "México",
        "tipo": "arquitectónica",
        "distancias": [
            {"Maravilla": "Gran Muralla China", "dist": 12000},
            {"Maravilla": "Petra", "dist": 10000},
            {"Maravilla": "Cristo Redentor", "dist": 7000},
            {"Maravilla": "Machu Picchu", "dist": 6000},
            {"Maravilla": "Coliseo de Roma", "dist": 9500},
            {"Maravilla": "Taj Mahal", "dist": 12500}
        ]
    },
    {
        "nombre": "Coliseo de Roma",
        "país": "Italia",
        "tipo": "arquitectónica",
        "distancias": [
            {"Maravilla": "Gran Muralla China", "dist": 8000},
            {"Maravilla": "Petra", "dist": 3000},
            {"Maravilla": "Cristo Redentor", "dist": 9600},
            {"Maravilla": "Machu Picchu", "dist": 10500},
            {"Maravilla": "Chichén Itzá", "dist": 9500},
            {"Maravilla": "Taj Mahal", "dist": 6000}
        ]
    },
    {
        "nombre": "Taj Mahal",
        "país": "India",
        "tipo": "arquitectónica",
        "distancias": [
            {"Maravilla": "Gran Muralla China", "dist": 6000},
            {"Maravilla": "Petra", "dist": 4000},
            {"Maravilla": "Cristo Redentor", "dist": 15000},
            {"Maravilla": "Machu Picchu", "dist": 15000},
            {"Maravilla": "Chichén Itzá", "dist": 12500},
            {"Maravilla": "Coliseo de Roma", "dist": 6000}
        ]
    },

    # Maravillas naturales
    {
        "nombre": "Montaña de la Mesa",
        "país": "Sudáfrica",
        "tipo": "natural",
        "distancias": [
            {"Maravilla": "Cataratas del Iguazú", "dist": 13000},
            {"Maravilla": "Parque Nacional de Komodo", "dist": 8000},
            {"Maravilla": "Amazonas", "dist": 15000},
            {"Maravilla": "Bahía de Ha Long", "dist": 11000},
            {"Maravilla": "Isla Jeju", "dist": 16000},
            {"Maravilla": "Río Subterráneo de Puerto Princesa", "dist": 12000}
        ]
    },
    {
        "nombre": "Cataratas del Iguazú",
        "país": ["Argentina", "Brasil"],
        "tipo": "natural",
        "distancias": [
            {"Maravilla": "Montaña de la Mesa", "dist": 13000},
            {"Maravilla": "Parque Nacional de Komodo", "dist": 9000},
            {"Maravilla": "Amazonas", "dist": 2500},
            {"Maravilla": "Bahía de Ha Long", "dist": 16000},
            {"Maravilla": "Isla Jeju", "dist": 19000},
            {"Maravilla": "Río Subterráneo de Puerto Princesa", "dist": 14000}
        ]
    },
    {
        "nombre": "Parque Nacional de Komodo",
        "país": "Indonesia",
        "tipo": "natural",
        "distancias": [
            {"Maravilla": "Montaña de la Mesa", "dist": 8000},
            {"Maravilla": "Cataratas del Iguazú", "dist": 9000},
            {"Maravilla": "Amazonas", "dist": 14000},
            {"Maravilla": "Bahía de Ha Long", "dist": 12000},
            {"Maravilla": "Isla Jeju", "dist": 7000},
            {"Maravilla": "Río Subterráneo de Puerto Princesa", "dist": 3000}
        ]
    },
    {
        "nombre": "Amazonas",
        "país": ["Brasil", "Colombia", "Perú", "Ecuador", "Venezuela", "Bolivia", "Guyana", "Surinam"],
        "tipo": "natural",
        "distancias": [
            {"Maravilla": "Montaña de la Mesa", "dist": 15000},
            {"Maravilla": "Cataratas del Iguazú", "dist": 2500},
            {"Maravilla": "Parque Nacional de Komodo", "dist": 14000},
            {"Maravilla": "Bahía de Ha Long", "dist": 13000},
            {"Maravilla": "Isla Jeju", "dist": 18000},
            {"Maravilla": "Río Subterráneo de Puerto Princesa", "dist": 10000}
        ]
    },
    {
        "nombre": "Bahía de Ha Long",
        "país": "Vietnam",
        "tipo": "natural",
        "distancias": [
            {"Maravilla": "Montaña de la Mesa", "dist": 11000},
            {"Maravilla": "Cataratas del Iguazú", "dist": 16000},
            {"Maravilla": "Parque Nacional de Komodo", "dist": 12000},
            {"Maravilla": "Amazonas", "dist": 13000},
            {"Maravilla": "Isla Jeju", "dist": 9000},
            {"Maravilla": "Río Subterráneo de Puerto Princesa", "dist": 13000}
        ]
    },
    {
        "nombre": "Isla Jeju",
        "país": "Corea del Sur",
        "tipo": "natural",
        "distancias": [
            {"Maravilla": "Montaña de la Mesa", "dist": 16000},
            {"Maravilla": "Cataratas del Iguazú", "dist": 19000},
            {"Maravilla": "Parque Nacional de Komodo", "dist": 7000},
            {"Maravilla": "Amazonas", "dist": 18000},
            {"Maravilla": "Bahía de Ha Long", "dist": 9000},
            {"Maravilla": "Río Subterráneo de Puerto Princesa", "dist": 16000}
        ]
    },
    {
        "nombre": "Río Subterráneo de Puerto Princesa",
        "país": "Filipinas",
        "tipo": "natural",
        "distancias": [
            {"Maravilla": "Montaña de la Mesa", "dist": 12000},
            {"Maravilla": "Cataratas del Iguazú", "dist": 14000},
            {"Maravilla": "Parque Nacional de Komodo", "dist": 3000},
            {"Maravilla": "Amazonas", "dist": 10000},
            {"Maravilla": "Bahía de Ha Long", "dist": 13000},
            {"Maravilla": "Isla Jeju", "dist": 16000}
        ]
    }
]


from grafo import Graph

# Crear grafos separados para cada tipo de maravilla
grafo_arquitectonico = Graph(dirigido=False)
grafo_natural = Graph(dirigido=False)

paises_arquitectonicos = set()
paises_naturales = set()

conteo_maravillas = {}
# Agregar maravillas y sus distancias a los grafos correspondientes
for maravilla in maravillas:
    paises = maravilla["país"]
    tipo = maravilla["tipo"]
    
    if maravilla["tipo"] == "arquitectónica":
        if isinstance(maravilla["país"], list):
            paises_arquitectonicos.update(maravilla["país"])
        else:
            paises_arquitectonicos.add(maravilla["país"])
            
        grafo_arquitectonico.insert_vertice(maravilla["nombre"])
            
        for distancia in maravilla["distancias"]:
            grafo_arquitectonico.insert_arista(maravilla["nombre"], distancia["Maravilla"], distancia["dist"])
            
    elif maravilla["tipo"] == "natural":
        if isinstance(maravilla["país"], list):
            paises_naturales.update(maravilla["país"])
        else:
            paises_naturales.add(maravilla["país"])
            
        grafo_natural.insert_vertice(maravilla["nombre"])
        
        for distancia in maravilla["distancias"]:
            grafo_natural.insert_arista(maravilla["nombre"], distancia["Maravilla"], distancia["dist"])

    if not isinstance(paises, list):
        paises = [paises]
    for pais in paises:
        if pais not in conteo_maravillas:
            conteo_maravillas[pais] = {"arquitectónica": 0, "natural": 0}
        conteo_maravillas[pais][tipo] += 1


# Calcular el árbol de expansión mínimo usando Kruskal para cada tipo de maravilla
arbol_arquitectonico = grafo_arquitectonico.kruskal("")
arbol_natural = grafo_natural.kruskal("")

# Mostrar los resultados
print("Árbol de expansión mínimo para maravillas arquitectónicas:")
for arista in arbol_arquitectonico:
    print(arista)

print("\nÁrbol de expansión mínimo para maravillas naturales:")
for arista in arbol_natural:
    print(arista)

paises_con_ambos_tipos = paises_arquitectonicos.intersection(paises_naturales)
print(f"\nPaíses que tienen tanto maravillas arquitectónicas como naturales: ", paises_con_ambos_tipos)


print("\nPaíses con más de una maravilla del mismo tipo:")
for pais, tipos in conteo_maravillas.items():
    for tipo, cantidad in tipos.items():
        if cantidad > 1:
            print(f"{pais} tiene {cantidad} maravillas de tipo {tipo}")
            
# grafo_arquitectonico.show_graph()
# grafo_natural.show_graph()
