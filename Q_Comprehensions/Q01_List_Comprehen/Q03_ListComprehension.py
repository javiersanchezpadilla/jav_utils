""" Convertir una lista de nombres a mayúsculas.

    [ expresión_final for elemento in lista_original if condicion ]
"""

nombres = ["ana", "beto", "carla"]
nombres_mayusculas = [ nombre.upper() for nombre in nombres]

print(nombres)
print(nombres_mayusculas)
