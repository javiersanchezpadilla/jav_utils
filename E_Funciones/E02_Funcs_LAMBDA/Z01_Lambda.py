""" Creación de una funcion lambda básica

    En ambos casos las funciones solo regresan un saludo
"""

def saludar():
    return "Hola a todos versión de función normal"

saludar_moderno = lambda: "Hola a todos versión de función LAMBDA"


print(saludar())

print(saludar_moderno())
