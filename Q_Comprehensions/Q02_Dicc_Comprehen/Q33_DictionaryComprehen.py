""" Transformar una lista en diccionario (con proceso)
    Tienes una lista de nombres y quieres saber cuántas letras tiene cada uno.

        nombres = ["Ana", "Beto", "Carla"]
"""

nombres = ["Ana", "Beto", "Carla"]

diccionario_nombres = {x:len(x) for x in nombres}

print('Lista de nombres', nombres)
print('Diccionario creado:', diccionario_nombres)

