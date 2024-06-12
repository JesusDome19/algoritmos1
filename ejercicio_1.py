# Desarrollar una función recursiva que permita listar los elementos de vector/lista de
# manera inversa al que están cargados. Preferentemente la función solo debe tener un
# parámetro que es la lista de elementos. 

from random import randint

def lista_inversa(lista):
    if lista == []: #vrifica si la lista esta vacia 
        return []
    else:
        return  [lista[-1]] + lista_inversa(lista[:-1]) #En cada recurcion saca el primer valor de la lista y lo agrga en la ultima pocision 
         


lista_de_numeros = []
#Ingreso los valores a la lista 
for numero in range(15):
    lista_de_numeros.append(randint(1, 99))
    
print("Lista original: ", lista_de_numeros) #Muestra la lista original

resultado = lista_inversa(lista_de_numeros)

print("\n Lista invertida: ", resultado)#Muestra la lista invertida