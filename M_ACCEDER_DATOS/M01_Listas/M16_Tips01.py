""" Si revisamos el siguiente código hay una trampa

    El problema con esta función es que una vez creada la lista, está quedará
    activa por el resto de la ejecución del código, por loque cada elemento
    agregado se aumentará a la misma lista, por eso en la segunda llamada
    se acumula con el resultado del primer resultado. La lista fue creada
    y reutilizable para siempre (no importa que su valor por defecto sea una
    list vacia)
"""

# Funcion con error de usar la misma lista (por lo que explico en los comentarios)
def add(x, items=[]):
    items.append(x)
    return items

print(add(1))           # [1]
print(add(2))           # [1, 2]


# Corrección de la función para que siempre sea una función nueva.
# Esto tambien aplica a diccionarios y conjuntos 
print('\n Solución de mejora con una nueva lista por ejecución')
def sumar(x, items_nuevos=None):
    if items_nuevos is None:
        items_nuevos = []      # Ahora si crea una nueva lista
    items_nuevos.append(x)
    return items_nuevos

print(sumar(1))       # [1] Ahora si son listas nuevas
print(sumar(2))       # [2]
