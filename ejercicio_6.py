from listas import search, remove, by_name, by_home
heroes = []
super_heroes = [
  {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
    "nombre": "Doctor Strange",
    "año_aparicion": 1963,
    "casa_comic": "DC Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
    "nombre": "Green Arrow",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
    "nombre": "Ant-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Hank Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos."
  }
]

#a. eliminar el nodo que contiene la información de Linterna Verde;
LV = remove(super_heroes, "nombre", "Linterna Verde")
print("lista de superhéroes: ")
for heroe in super_heroes:
    print(heroe)

#b. mostrar el año de aparición de Wolverine;
wolverin = search(super_heroes, "nombre", "Wolverine")
print( "\nWolverine aparecion en el año", super_heroes[wolverin]["año_aparicion"])

#c. cambiar la casa de Dr. Strange a Marvel;
stringe = search(super_heroes, "nombre", "Doctor Strange")
print(f"\nLa casa del Dr. Strange era ", super_heroes[stringe]["casa_comic"]) 
casa_marvel = super_heroes[stringe]["casa_comic"] = "Marvel Comics"
print(f"Ahora la casa del Dr. Stringe es {casa_marvel}")

#d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
for index, heroe in enumerate(super_heroes):
    if "traje" in heroe["biografia"] or "armadura" in heroe["biografia"]:
        print(f"\n{index}, {heroe["nombre"]}, {heroe["biografia"]}")
        
#e.mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;

super_heroes.sort(key=by_name)

print("\nSuper heroes que aparecieron antes de 1963: ")
for heroe in super_heroes:
    if heroe["año_aparicion"] < 1963:
        print(f" {heroe["nombre"]}, {heroe["año_aparicion"]}")        
        

#f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
cap_marvel = search(super_heroes, "nombre", "Capitana Marvel")
mu_mar = search(super_heroes, "nombre", "Mujer Maravilla")
print(f"\nLa casa de la Capitana Marvel es {super_heroes[cap_marvel]["casa_comic"]} y la casa de la Mujer Maravilla es {super_heroes[mu_mar]["casa_comic"]}")


#g.mostrar toda la información de Flash y Star-Lord;
flash = search(super_heroes, "nombre", "Flash")
star_lord =  search(super_heroes, "nombre", "Star-Lord")
print("\nInformacion de Flash y Star-Lord")
print(f"{super_heroes[flash]} \n {super_heroes[star_lord]}")


#h. listar los superhéroes que comienzan con la letra B, M y S;
print("\nLista de los superhéroes que comienzan con B, M, S: ")
for index, heroe in enumerate(super_heroes):
    if heroe["nombre"].startswith(("B", "M", "S")):
        print(index, heroe["nombre"])
 

dc_cant = 0
marvel_cant = 0 
super_heroes.sort(key=by_home)

#i. determinar cuántos superhéroes hay de cada casa de comic.
for heroe in super_heroes:
    if heroe["casa_comic"].startswith(("DC")):
        dc_cant += 1
    if heroe["casa_comic"].startswith(("Marvel")):
        marvel_cant += 1 
        
print(f"\nLa casa de DC comic cuenta con {dc_cant} super heroes y marvel cuenta con {marvel_cant} super heroes")