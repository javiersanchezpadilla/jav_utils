""" Ejemplo del uso de la funcion enumerate para iterar sobre una lista
    de diccionarios y obtener tanto el indice como el valor de cada elemento.
    
    En este ejercicio se utilizará una lista de diccionarios que representan
    diferentes personas con sus respectivas edades. Se aplicará enumerate para
    obtener el índice y el nombre de cada persona.

    variable_resultado = enumerate(iterable, start=0)
    - iterable: una colección de elementos (lista, tupla, etc.) que se va a iterar.
    - start: el valor inicial del índice (opcional, por defecto es 0).
    
    El resultado de enumerate es un objeto iterable que contiene tuplas con
    el índice y el elemento correspondiente.
"""

def enumerar_personas(personas):
    """
    Itera sobre una lista de diccionarios y devuelve una lista de tuplas
    con el índice y el nombre de cada persona.
    
    :param personas: Lista de diccionarios con información de personas.
    :return: Lista de tuplas con el índice y el nombre de cada persona.
    """
    return list(enumerate(personas, start=1))       

# Ejemplo de uso    
personas = [
    {'nombre': 'Juan', 'edad': 20},
    {'nombre': 'Ana', 'edad': 17},
    {'nombre': 'Luis', 'edad': 22},
    {'nombre': 'María', 'edad': 15},
    {'nombre': 'Pedro', 'edad': 19}
]

enumeradas = enumerar_personas(personas)
print(enumeradas)  # [(1, {'nombre': 'Juan', 'edad': 20}), (2, {'nombre': 'Ana', 'edad': 17}), ...]     