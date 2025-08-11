""" Uso de la funcion filter para seleccionar datos
    de una lista de diccionarios.
    
    En este ejercicio se utilizará una lista de diccionarios que representan
    diferentes personas con sus respectivas edades. Se aplicará un filtro para
    seleccionar solo aquellas personas cuya edad sea mayor o igual a 18 años.

    variable_resultado = filter(funcion, iterable)
    - funcion: una función que devuelve True o False.
    - iterable: una colección de elementos (lista, tupla, etc.) que se va a filtrar.
    
    El resultado de filter es un objeto iterable que contiene solo los elementos
    para los cuales la función devolvió True.
    Para convertirlo en una lista, se puede usar la función list().
"""

def filtrar_mayores_de_edad(personas):
    """
    Filtra una lista de diccionarios para obtener solo aquellos
    que representan personas mayores de edad (18 años o más).
    
    :param personas: Lista de diccionarios con información de personas.
    :return: Lista filtrada de personas mayores de edad.
    """
    return list(filter(lambda persona: persona['edad'] >= 18, personas))

# Ejemplo de uso    
personas = [
    {'nombre': 'Juan', 'edad': 20},
    {'nombre': 'Ana', 'edad': 17},
    {'nombre': 'Luis', 'edad': 22},
    {'nombre': 'María', 'edad': 15},
    {'nombre': 'Pedro', 'edad': 19}
]

mayores_de_edad = filtrar_mayores_de_edad(personas)
print(mayores_de_edad)  # [{'nombre': 'Juan', 'edad': 20}, {'nombre': 'Luis', 'edad': 22}, {'nombre': 'Pedro', 'edad': 19}] 
