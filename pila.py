
class stack:
    def __init__(self): #PILA VASIA  
        self.__elements = []
        
    def push(self, element): #  INGRESA LOS ELEMENTOS A LA PILA
        self.__elements.append(element)
    
    def pop(self): #ELIMINA ELEMENTOS DE LA LISTA 
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None 
        
    
    def on_top(self): # DEBUELVE LOS ELEMENTOS DE LA PILA
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None
    
    
    def size(self): # TAMAÑO DE LA PILA 
        return len(self.__elements)
    