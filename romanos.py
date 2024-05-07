#Desarrollar una función que permita convertir un número romano en un número decimal.

def romano_decimal(numero):
    num_romanos = { "I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000} #Lista de los numeros romanos equivalentes en decimal.

    if len(numero) == 0: #Berifico si la lista tiene elemetos.
        return 0

    if len(numero) == 1: #Berifico la cantidad de tiene el la vatiable, si solo es un valor retorno su equivalente en decimal.
        return num_romanos[numero]

    if num_romanos[numero[1]] > num_romanos[numero[0]]: #berifico que si el valor de la posicion 1 es mayor a el de la posicion 0
        return num_romanos[numero[1]] - num_romanos[numero[0]] + romano_decimal(numero[2:])

    else:
        return num_romanos[numero[0]] + romano_decimal(numero[1:])

valores = "MDCCCXVI"
print(f"El número romano {valores} es equivalente a {romano_decimal(valores)} en decimal.") #muestro el numero al cual equivalen los numero romanos  
