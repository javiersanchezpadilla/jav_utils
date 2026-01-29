""" Lo importante de este ejemplo es el uso de la función lambda
    para crear una lista de cuadrados de una lista de números.
    Se muestran tres formas de lograrlo: con un bucle for,
    con una comprensión de lista y con la función map.
    
    Map devuelve una lista y requiere dos argumentos map(una_función, iterable)
    """


num = [1, 2, 3, 4, 5, 6 ]

print("Lista original              ", num)
# Version 1 para crear una lista de cuadrados
cuadrados = []
for i in num:
    cuadrados.append(i ** 2)

print("Forma 1 de lista al cuadrado",cuadrados)


# Version 2 para crear una lista de cuadrados
# aunque esto solo aplica a una lista continua de
# valores numericos
cuadrados = [i ** 2 for i in num]
print("Forma 2 de lista al cuadrado",cuadrados)

# Version 3 para crear una lista de cuadrados
cuadrados = list(map(lambda x: x ** 2, num))
print("Forma 3 de lista al cuadrado",cuadrados)