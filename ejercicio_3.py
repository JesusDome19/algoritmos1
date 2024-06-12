# Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros, colores de sable de luz usados y especie.
# implementar las funciones necesarias para resolver las actividades enumeradas a continuación:


from Jedi import jedis
from listas import by_name, by_species, search

jedis_ordenados_species = jedis
jedis_ordenados_name = jedis

# a) listado ordenado por nombre 
jedis_ordenados_name.sort(key=by_name)
# for jedi in jedis_ordenados_name:
#     print(jedi)

#listado ordenado por especie;
# jedis_ordenados_species.sort(key=by_species)
# for jedi in jedis_ordenados_species:
#     print(jedi)

# b) mostrar toda la información de Ahsoka Tano y Kit Fisto;

# Ahsoka = search(jedis_ordenados_name, "name", "Ahsoka Tano")
# print(jedis_ordenados_name[Ahsoka])
# kitFisto = search(jedis_ordenados_name, "name", "Kit Fisto")
# print(jedis_ordenados_name[kitFisto])

# c) mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# print("\nLos padawan de Yoda y Luke Skywalker son: ")
# for aprendises in jedis_ordenados_name:
#     if aprendises['master'] in ("Yoda", "Luke Skywalker"):
#         print(aprendises)
        
# d) mostrar los Jedi de especie humana y twi'lek;
# for jodis_especie in jedis_ordenados_name:
#     if jodis_especie['species'] in ("Human", "Twi'lek"):
#         print(jodis_especie)
    
# e) listar todos los Jedi que comienzan con A;
# JedisConA = []
# for jedis_A in jedis_ordenados_name:
#     if jedis_A['name'].startswith(("A")):
#         JedisConA.append(jedis_A)

# print(JedisConA)

# f) mostrar los Jedi que usaron sable de luz de más de un color;
# for sables_jodi in jedis_ordenados_name:
#     colors = sables_jodi["lightsaber_color"]
#     color = colors.split()
#     if len(color) >= 2:
#         print(colors)
            
# g) indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# for sables_jodi in jedis_ordenados_name:
#     if sables_jodi["lightsaber_color"] is not None:
#         if sables_jodi["lightsaber_color"].startswith(("Yellow", "Purple")):
#             print(sables_jodi)
                  
        
            
# h) indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
print("\nLos padawan de Qui-Gon Jin y Mace Windu son: ")
for aprendises in jedis_ordenados_name:
    if aprendises["master"] is not None:
        if aprendises['master'] in ("Qui-Gon Jin", "Mace Windu"):
            print(aprendises)
    else:
        print("Qui-Gon Jin y Mace Windu no tienen ningun padawans")
        break

# i) Mostrar todos los Jedi que tengan el ranking de Grand Master.
print("\n Los jedis Gand Master son: ")
for jedis_grand_master in jedis_ordenados_name:
    if jedis_grand_master["rank"] == "Grand Master":
        print(jedis_grand_master)
    