class personaje:

    def __init__(self, nombre, cant_peli):
        self.nombre = nombre
        self.cant_peli = cant_peli
    

    def __str__(self):
        return f"{self.nombre} - {self.cant_peli}"