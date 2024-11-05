#El general Hux es la persona encargada de administrar todas las operaciones de la base Starki-
#ller, para lo cual nos solicita desarrollar un algoritmo que permita controlar las actividades que
#se realizan, contemplando lo siguiente:
#a.debe contemplar distintas prioridades para el control de operaciones de acuerdo al siguien-
#te criterio: pedidos de líder supremo Snoke y de Kylo Ren nivel tres, de capitán Phasma
#nivel dos y el resto de las operaciones nivel a cargo de los generales de la base de nivel uno;
#b.de cada actividad se conoce quien es el encargado, una descripción, la hora y opcional-
#mente la cantidad de Stormtroopers requeridos;
#c.utilizar una cola de prioridad para administrar las distintas operaciones, debe cargar al
#menos ocho: dos de nivel tres, cuatro de nivel dos y cuatro de nivel uno;
#d.opcionalmente se podrán agregar operaciones luego de atender una;
#e.realizar la atención de las operaciones de la cola;
#f.luego de atender la quinta operación, agregar una operación solicitada por capitán Phasma
#para revisión de intrusos en el hangar B7 que requiere 25 Stormstroopers;
#g.luego de atender la sexta operación, agregar una operación solicitada por el líder supremo Snoke para destruir el planeta Takodana.

from heap import HeapMax, HeapMin

def ordenar_por_operacion(lista_diccionarios):
    # Ordenamos la lista in-place utilizando el método sort()
    lista_diccionarios.sort(key=lambda x: x['operacion'])
    return lista_diccionarios

def cargardatos(num):
    encargado = input("Ingrese el nombre del encargado de la operacion: ")
    descripcion = input("Ingresar descripcion de la operacion: ")
    hora = input("Ingresar hora de la operacion: ")
    stormtroopers_requeridos = input("Ingresar la cantidad de stormtroopers_requeridos necesarios: ")

    return  {"encargado": encargado, "descripcion": descripcion, "operacion": num +1, "hora": hora, "stormtroopers_requeridos":stormtroopers_requeridos}


operaciones = [
    {   "encargado": "General",
        "descripcion": "Inspeccionar hangares",
        "operacion": 6,
        "hora": "13:00",
        "stormtroopers_requeridos": 100},
    
    {   "encargado": "Kylo Ren",
        "descripcion": "Operación de control total del sistema",
        "operacion": 1,
        "hora": "08:00",
        "stormtroopers_requeridos": 500},
    
    {   "encargado": "Capitán Phasma",
        "descripcion": "Asalto al puesto rebelde",
        "operacion": 2,
        "hora": "10:00",
        "stormtroopers_requeridos": 300},
    
    {   "encargado": "General",
        "descripcion": "Entrenamiento con sable de luz",
        "operacion": 8,
        "hora": "10:00"},
    
    {   "encargado": "Capitán Phasma",
        "descripcion": "Supervisión de las operaciones de suministro",
        "operacion": 4,
        "hora": "14:00"},
    
    {   "encargado": "General",
        "descripcion": "Mantenimiento de la flota estelar",
        "operacion": 5,
        "hora": "16:00"},
    
    
    {   "encargado": "Snoke",
        "descripcion": "Vigilancia del perímetro de la base",
        "operacion": 3,
        "hora": "12:00",
        "stormtroopers_requeridos": 150},
    
    {   "encargado": "General",
        "descripcion": "Plan de defensa",
        "operacion": 7,
        "hora": "15:00"}
    
]

prioridades = [
   
    {'encargado': 'Kylo Ren', 'nivel': 3},
    {'encargado': 'Capitán Phasma', 'nivel':2},
    {'encargado': 'Snoke', 'nivel': 3},
    {'encargado': 'General', 'nivel': 1}
]

from random import randint
from cola import Queue

heap = HeapMax()
cola = Queue()
cola1 = Queue()

for prioridad in prioridades:
    heap.arrive(prioridad["encargado"], prioridad["nivel"])

pos = heap.sort()
print(pos) 

ordenados = ordenar_por_operacion(operaciones)
# print(ordenados)

for posicion in pos:
    for operacion in ordenados:
        if posicion[1] == operacion["encargado"]:
            posicion.append(operacion)
    cola.arrive(posicion)
    
            

oper = int(input("Ingresar en numero de la operacion reallizada: "))
# oper = 1
nuevos_datos = None

numero = randint(8, 20)
while cola.size() > 0:
    responsable = cola.attention()
    for index, misiones in enumerate(responsable[2:]):
        if misiones["operacion"] == oper:
            print(f"la operacion eliminada {misiones}")
            responsable.pop(index+2)
            Agre_Oper = input("Desea agregar una nueva operacion: ")
            if Agre_Oper.capitalize() == "Si":
                nuevos_datos = cargardatos(numero)
            # oper += 1
    cola.arrive(responsable)

while (cola1.size() > 0):
    dato = cola1.attention()
    if nuevos_datos is not None:
        if dato[1] in nuevos_datos["encargado"]:
            dato.append(nuevos_datos)
        for mision in dato[2:]:
            
            if mision["operacion"] == 5:
                pass
            else:
                mision_nueva = {"encargado": "Capitán Phasma", "descripcion": "Revisar si hay intrusos en el hangar B7.", "operacion": 10, "hora": "08:00", "stormtroopers_requeridos":25}
                dato.append(mision_nueva)
            if mision["operacion"] == 6:
                pass
            else:
                mision_nueva = {"encargado": "Snoke", "descripcion": "Destruir el planeta Takodana.", "operacion": 11, "hora": "08:00", "stormtroopers_requeridos":25000}
                dato.append(mision_nueva)
    cola.arrive(dato)
print("   ")

while (cola.size() > 0):
    print(cola.attention())