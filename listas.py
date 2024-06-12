#! criterios de orden
def by_name(item):
    return item['name']

def by_hegiht(item):
    return item['altura']

def by_species(item):
    return item["species"]

def by_temp(item):
    return item['temp']

def by_torneos(item):
    return item['torneos_ganados']


#BUSCAR ELEMENTOS SIMPLES
def search(list_values, criterio, value):
    for index, element in enumerate(list_values):
        if element[criterio] == value:
            return index
        
#! eliminar un elemento de la lista
def remove(list_values, criterio, value):
    index = search(list_values, criterio, value)
    if index is not None:
        return list_values.pop(index)
    
#! barrido
def show_list(title, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index, elemento)
    print()
 
      
# BARRIDO DE LISTA DE LISTA
def show_list_list(title, subtitle, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index, elemento['nombre'])
        print(f"    {subtitle}")
        for second_index, second_element in enumerate(elemento['pokemons']):
            print('    ', second_index, second_element)
    print()