""" SOBRE ESCRIBIR FUNCIONES CON FUNCIONES LAMBDA

    Sobre escritura de una función interconstruida
    ----------------------------------------------
    En este ejemplo vamos a modificar el comportamiento de una función
    interconstruida, en este caso la función 'print()' con una función LAMBDA
"""

print = lambda x:__builtins__.print('>>>>>>', x)

print("Hola a todos")
