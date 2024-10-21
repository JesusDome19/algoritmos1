
criaturas = [
    {"Nombre": "Ceto", "Derrotado_por": "-"},
    {"Nombre": "Tifon", "Derrotado_por": "Zeus"},
    {"Nombre": "Equidna", "Derrotado_por": "Argos Panoptes"},
    {"Nombre": "Dino", "Derrotado_por": "-"},
    {"Nombre": "Pefredo", "Derrotado_por": "-"},
    {"Nombre": "Enio", "Derrotado_por": "-"},
    {"Nombre": "Escila", "Derrotado_por": "-"},
    {"Nombre": "Caribdis", "Derrotado_por": "-"},
    {"Nombre": "Euriale", "Derrotado_por": "-"},
    {"Nombre": "Esteno", "Derrotado_por": "-"},
    {"Nombre": "Medusa", "Derrotado_por": "Perseo"},
    {"Nombre": "Ladon", "Derrotado_por": "Heracles"},
    {"Nombre": "Aguila del Caucaso", "Derrotado_por": "-"},
    {"Nombre": "Quimera", "Derrotado_por": "Belerofonte"},
    {"Nombre": "Hidra de Lerna", "Derrotado_por": "Heracles"},
    {"Nombre": "Leon de Nemea", "Derrotado_por": "Heracles"},
    {"Nombre": "Esfinge", "Derrotado_por": "Edipo"},
    {"Nombre": "Dragon de la Colquida", "Derrotado_por": "-"},
    {"Nombre": "Cerbero", "Derrotado_por": "-"},
    {"Nombre": "Cerda de Cromion", "Derrotado_por": "Teseo"},
    {"Nombre": "Ortro", "Derrotado_por": "Heracles"},
    {"Nombre": "Toro de Creta", "Derrotado_por": "Teseo"},
    {"Nombre": "Jabali de Calidon", "Derrotado_por": "Atalanta"},
    {"Nombre": "Carcinos", "Derrotado_por": "-"},
    {"Nombre": "Gerion", "Derrotado_por": "Heracles"},
    {"Nombre": "Cloto", "Derrotado_por": "-"},
    {"Nombre": "Laquesis", "Derrotado_por": "-"},
    {"Nombre": "Atropos", "Derrotado_por": "-"},
    {"Nombre": "Minotauro de Creta", "Derrotado_por": "Teseo"},
    {"Nombre": "Harpias", "Derrotado_por": "-"},
    {"Nombre": "Argos Panoptes", "Derrotado_por": "Hermes"},
    {"Nombre": "Aves del Estinfalo", "Derrotado_por": "-"},
    {"Nombre": "Talos", "Derrotado_por": "Medea"},
    {"Nombre": "Sirenas", "Derrotado_por": "-"},
    {"Nombre": "Piton", "Derrotado_por": "Apolo"},
    {"Nombre": "Cierva de Cerinea", "Derrotado_por": "-"},
    {"Nombre": "Basilisco", "Derrotado_por": "-"},
    {"Nombre": "Jabali de Erimanto", "Derrotado_por": "-"},
]

from  arbol_avl import BinaryTree 

tree = BinaryTree()
tree_dioses = BinaryTree()

for criatura in criaturas:
    tree.insert_node(criatura["Nombre"], criatura)
    tree_dioses.insert_node(criatura["Derrotado_por"], criatura)
    

print(" Lista de las criaturas y por quien fueron derrotados")
tree.inorden_criaturas()

#b.se debe permitir cargar una breve descripción sobre cada criatura;
descrip = "gigante de bronce en la mitología griega, creado por el dios Hefesto para proteger la isla de Creta."
value_to_delete = 'Talos'
delete_value, extra_info = tree.delete_node(value_to_delete)
extra_info = extra_info, {"Descripcion": descrip}
tree.insert_node(delete_value, extra_info)

#c. Mostrar toda la información de la criatura Talos;
print()
tree.criatura_search("Talos")

# listar las criaturas derrotadas por Heracles;
print("\nLista de criaturas derrotadas por Heracles")
tree_dioses.inorden_dioses_start_with("Heracles")

# listar las criaturas que no han sido derrotadas;
print("\nLista de criaturas que no fueron derrotadas")
tree_dioses.inorden_dioses_start_with("-")

# además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
criaturas_mitologicas = [
    {"nombre": "Ceto", "capturada": "No fue capturada, es una diosa primigenia del mar"},
    {"nombre": "Tifon", "capturada": "Derrotado por Zeus"},
    {"nombre": "Equidna", "capturada": "No fue capturada, muerta por Argos Panoptes"},
    {"nombre": "Dino", "capturada": "No fue capturada"},
    {"nombre": "Pefredo", "capturada": "No fue capturada"},
    {"nombre": "Enio", "capturada": "No fue capturada"},
    {"nombre": "Escila", "capturada": "No fue capturada, sobrevivió"},
    {"nombre": "Caribdis", "capturada": "No fue capturada, sobrevivió"},
    {"nombre": "Euriale", "capturada": "No fue capturada"},
    {"nombre": "Esteno", "capturada": "No fue capturada"},
    {"nombre": "Medusa", "capturada": "Perseo"},
    {"nombre": "Ladon", "capturada": "Heracles (mató a Ladón)"},
    {"nombre": "Aguila del Caucaso", "capturada": "Heracles"},
    {"nombre": "Quimera", "capturada": "Belerofonte"},
    {"nombre": "Hidra de Lerna", "capturada": "Heracles"},
    {"nombre": "Leon de Nemea", "capturada": "Heracles"},
    {"nombre": "Esfinge", "capturada": "Edipo (resolvió su enigma, provocando que la Esfinge se suicidara)"},
    {"nombre": "Dragon de la Colquida", "capturada": "Jasón (Medea lo durmió con un hechizo)"},
    {"nombre": "Cerbero", "capturada": "Heracles (lo llevó vivo al rey Euristeo como parte de sus trabajos)"},
    {"nombre": "Cerda de Cromion", "capturada": "Teseo"},
    {"nombre": "Ortro", "capturada": "Heracles"},
    {"nombre": "Toro de Creta", "capturada": "Heracles"},
    {"nombre": "Jabali de Calidon", "capturada": "Atalanta y Meleagro"},
    {"nombre": "Carcinos", "capturada": "Heracles (durante la lucha con la Hidra)"},
    {"nombre": "Gerion", "capturada": "Heracles"},
    {"nombre": "Cloto", "capturada": "No fue capturada (es una diosa del destino)"},
    {"nombre": "Laquesis", "capturada": "No fue capturada (es una diosa del destino)"},
    {"nombre": "Atropos", "capturada": "No fue capturada (es una diosa del destino)"},
    {"nombre": "Minotauro de Creta", "capturada": "Teseo"},
    {"nombre": "Argos Panoptes", "capturada": "Hermes"},
    {"nombre": "Harpias", "capturada": "Boreadas (Calais y Zetes, pero fueron liberadas por Iris)"},
    {"nombre": "Aves del Estinfalo", "capturada": "Heracles"},
    {"nombre": "Talos", "capturada": "Medea (lo mató con un hechizo)"},
    {"nombre": "Sirenas", "capturada": "No fueron capturadas (sobrevivieron al encuentro con Odiseo y los Argonautas)"},
    {"nombre": "Piton", "capturada": "Apolo"},
    {"nombre": "Cierva de Cerinea", "capturada": "Heracles"},
    {"nombre": "Basilisco", "capturada": "No hay un héroe específico asociado con su captura"},
    {"nombre": "Jabali de Erimanto", "capturada": "Heracles"}
]

print("\nLos nodos con el campo capturada: ")
for criatura in criaturas_mitologicas:
    delete_value, extra_info = tree.delete_node(criatura["nombre"])
    extra_info = extra_info, {"capturada": criatura["capturada"]}
    tree.insert_node(delete_value, extra_info)
    tree.criatura_search(criatura["nombre"])


#modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
#Erimanto indicando que Heracles las atrapó;
print("\nLista de los nodos de las criatruas 'Cerbero, Toro de Creta, Cierva de Cerinea, Jabal de Erimanto': \n")
criaturas_modificar = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabal de Erimanto"]
for criatura in criaturas_modificar:
    delete_value, extra_info = tree.delete_node(criatura)
    if delete_value is not None:
        extra_info = extra_info[0], {"capturada": "Heracles"}
        tree.insert_node(delete_value, extra_info)
    tree.criatura_search(criatura)

#eliminar al Basilisco y a las Sirenas;
criaturasEliminar = ["Basilisco", "Sirenas"]
for nombre in criaturasEliminar:
    tree.delete_node(nombre)
    pos = tree.search(nombre)
    if pos is None:
        print(f"\nSe elimino correctamente {nombre}")


#modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;  
print()
delete_value, extra_info = tree.delete_node("Aves del Estinfalo")
extra_info[0]["Derrotado_por"]  = "Heracles"
tree.insert_node(delete_value, extra_info)
tree.criatura_search("Aves del Estinfalo")      


# modifique el nombre de la criatura Ladón por Dragón Ladón;
print("\nAntes de modidficar el nombre: ") 
tree.criatura_search("Ladon")
delete_value, extra_info = tree.delete_node("Ladon")

new_name = "Dragon Ladon"
delete_value = new_name
extra_info[0]["Nombre"] = new_name
tree.insert_node(delete_value, extra_info)
print("Despues de modificar el nombre: ")
tree.criatura_search("Dragon Ladon")

#realizar un listado por nivel del árbol;
print("\nListado por nivel: ")
tree.by_level()

#n. muestre las criaturas capturadas por Heracles
print("\n Lista de las criaturas capturadas por Heracles: ")
tree.search_dioses("Heracles")
