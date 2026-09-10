""" FILTER 

    Permite seleccionar elementos, mantiene solamente aquellos elementos
    que cumplen una condición.
"""

numeros = [1, 2, 3, 4]
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)
