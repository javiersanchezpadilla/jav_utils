""" Manejo de los arguemntos posicionales ilimitados

    Pensemos en la siguiente función

        def suma(n1, n2):
            return n1 + n2

        print(suma(10, 20))

    Si queremos sumar ahora cuatro valores, tendriamos que cambiar la función

        def suma(n1, n2, n3, n4):
            return n1 + n2 + n3 + n4

        print(suma(10, 20, 5, 5))
    
    Si quisieramos para seis valores

        def suma(n1, n2, n3, n4, n5, n6):
            return n1 + n2 + n3 + n4 + n5 + n6

        print(suma(10, 20, 2, 1, 1, 10))

    Para resolver este problema es que haremos uso de los argumentos ilimitador 
        *args   args es el nombre por convención pero puede ser el nombre que
                deseemos por ejemplo *perro *argumentos
       
"""

def suma(*args):
    print(args)         # El dato que recibimos (una tupla)
    print(type(args))   # El tipo de datos pertenece a <class tuple>
    suma = 0
    for valor in args:
        suma += valor
    return suma


print(suma(1))
print(suma(1, 2))
print(suma(1, 2, 3))
print(suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
