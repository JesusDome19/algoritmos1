# 2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:
# a) Contar cuantas especies hay;
# b) Determinar cuantos descubridores distintos hay;
# c) Mostrar todos los dinosaurios que empiecen con T;
# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;

from pila import stack

dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": 7000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": 6000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": 15,
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": 56000,
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": 5000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": 10000,
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": 2000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": 23000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": 15000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": 6000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": 2500,
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": 1500,
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": 2700,
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": 5000,
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": 25,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": 200,
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": 450,
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": 15000,
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]

dinos = stack()
dinos_2 = stack()
Dino_3 = stack()

# cargo la pila con los datos de la lista
for dinossurio in dinosaurios:
    dinos.push(dinossurio)


# a) Contar cuantas especies hay;
especies_unicas = set()
while (dinos.size() > 0):
    especies = dinos.pop()
    especies_unicas.add(especies['especie'])
    dinos_2.push(especies)   
print(f"Entotal hay {len(especies_unicas)} especies de dinosaurios en la lista")

# b) Determinar cuantos descubridores distintos hay;
descubridores = 0
while (dinos_2.size() > 0):
    descubridor = dinos_2.pop()
    # especies_unicas.add(descubridor['descubridor'])
    if descubridor['descubridor'].startswith(( "Barnum Brown", "Othniel Charles Marsh", "Henry Fairfield Osborn", "Elmer S. Riggs", "Ernst Stromer", "William Parks", "José Bonaparte", "Lawrence Lambe", "Evgeny Maleev", "Douglas A. Lawson", "Mary Anning", "William Conybeare")) :
        descubridores += 1
    else:
        descubridores += 1
    dinos.push(descubridor)   
print(f"\nEntotal hay {descubridores} descubridores diferentes en la lista")

# c) Mostrar todos los dinosaurios que empiecen con T;
print("\nLos dinosaurios que su numbre empieza con T son:")
while (dinos.size() > 0):
    dino = dinos.pop()
    if dino['nombre'].startswith(("T")):
        print(dino)
        dinos_2.push(dino)
    dinos_2.push(dino)
    

    
# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
print("\n Los dinosaurios que pean menos de 275kg son: ")
while (dinos_2.size() > 0):
    dino_peso = dinos_2.pop()
    if dino_peso["peso"] < 275:
        print(dino_peso)
    dinos.push(dino_peso)


# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;
while (dinos.size() > 0):
    dino_AQS = dinos.pop()
    if dino_AQS["nombre"].startswith(("A", "Q", "S")):
        dinos_2.push(dino_AQS)
    else:
        Dino_3.push(dino_AQS)

print("\n Los dinosaurios que comienza con la letra A, Q, S son: ")
while (dinos_2.size() > 0):
    print(dinos_2.pop())
        