""" Si revisamos el siguiente código hay una trampa

    El problema con esta función es que una vez creado el diccionario, 
    esté quedará activo por el resto de la ejecución del código, por 
    lo que cada elemento agregado se aumentará, por eso en la segunda llamada
    se acumula con el resultado del primer resultado. el diccionario fue creado
    y reutilizable para siempre (no importa que su valor por defecto sea un
    diccionario vacio)
"""

# Funcion con error que usa el mismo diccionario
def track(key, d={}):
    d[key] = True
    return d

print(track("a"))           # {'a': True}
print(track("b"))           # {'a': True, 'b': True}


# Corrección de la función para que siempre sea un diccionario nuevo
print('\n Solución de mejora con un nuevo diccionario por ejecución')

def track_mejorado(key, d_mejorado=None):
    if d_mejorado is None:
        d_mejorado = {}
    d_mejorado[key] = True
    return d_mejorado

print(track_mejorado("a"))           # {'a': True}  Diccionarios nuevo (no acumulado)
print(track_mejorado("b"))           # {'b': True}
