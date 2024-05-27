#Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
#strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
#permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.

from pila import stack

pila = stack()
P_E_V = stack()
P_E_VII = stack()  

personajes_episodio_v = [
    "Luke Skywalker", "Darth Vader", "Princess Leia", "Han Solo", "Chewbacca","C-3PO", "R2-D2",
    "Yoda", "Emperor Palpatine", "Lando Calrissian", "Boba Fett", "Obi-Wan Kenobi (voz)",
    "Wedge Antilles", "Admiral Piett", "Bossk", "Dengar", "IG-88", "Zuckuss", "Wampa", "Tauntaun"
]

personajes_episodio_vii = [
    "Rey", "Finn", "Kylo Ren", "Han Solo", "Princess Leia", "Poe Dameron", "Chewbacca", "BB-8",
    "C-3PO", "R2-D2", "Maz Kanata", "Supreme Leader Snoke", "Captain Phasma", "General Hux", "Lor San Tekka", 
    "Admiral Statura", "Snap Wexley", "Unkar Plutt", "Constable Zuvio", "Teedo"
]

personajes_episodio_v.sort()
personajes_episodio_vii.sort()

for personaje in personajes_episodio_v:
    P_E_V.push(personaje)


for personaje in personajes_episodio_vii:
    P_E_VII.push(personaje)

intersec = []

while (P_E_V.size() > 0):
    personaje = P_E_V.pop()

    while (P_E_VII.size() > 0):

        protagonista = P_E_VII.pop()

        if personaje == protagonista:
           
           intersec.append(personaje)
           
        else:
            pila.push(protagonista)
    
    while (pila.size() > 0):
        P_E_VII.push(pila.pop())

    
print("Personajes que aparecen en ambos episodios:")
for personaje in intersec:
    print(personaje)