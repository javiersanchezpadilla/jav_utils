""" Transforma una lista con map

    Permite aplicar una función a cada elemento de la lista
    Resultado: [1, 4, 9, 16]
"""

numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))

print(cuadrados)
