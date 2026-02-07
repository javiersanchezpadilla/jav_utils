""" El Desempaquetado usando '*'

    Aqui haremos uso de la variable "descartable" o "variable muda" _
    a veces, tienes una lista larga pero solo te interesan el primero y el 
    último elemento. Aquí usamos el asterisco * (que en este contexto significa 
    "el resto").

    Analogía: 
    ---------
    Imagina que recibes un regalo: te quedas con el moño, con el juguete, y todo 
    el papel de regalo sobrante lo amontonas en un rincón.
"""

# Una lista de calificaciones
notas = [10, 9, 8, 7, 6, 5]

# Queremos la mejor, la peor y guardar las demás en una lista aparte
mejor, *el_resto, peor = notas

print(f"La mejor nota fue: {mejor}")
print(f"La peor nota fue: {peor}")
print(f"Las notas intermedias fueron: {el_resto}")
