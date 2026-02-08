""" SOBRE ESCRIBIR FUNCIONES CON FUNCIONES LAMBDA

    Sobre escritura de una función normal.
    --------------------------------------
    En este caso, aunque la función ya existe si la sobreescribimos, la que
    python considerará será la definida como LAMBDA, notar que ambas funciones
    tienen el mismo nombre por lo que se sobre escriben.
"""

def saludar():
    return "Hola a todos versión de función normal"

            # Aquí sobre escribimos el método
saludar = lambda: "Hola a todos versión de función LAMBDA"


print(saludar())
