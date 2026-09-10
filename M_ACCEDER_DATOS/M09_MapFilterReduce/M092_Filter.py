""" MAP. FILTER Y REDUCE

    Las tres son funciones de orden superior (higher-order functions) en 
    Python, lo que significa que toman una función y una secuencia de datos 
    como argumentos. La diferencia principal radica en la intención de 
    transformación de cada una:Resumen Visual de la Diferencia
    **) map(): Transforma cada elemento. (Entran N elementos, salen N 
        elementos transformados).
    **) filter(): Selecciona según una condición. (Entran N elementos, 
        salen <=N elementos que cumplen un criterio).
    **) reduce(): Acumula o combina todo en un solo resultado. 
        (Entran N elementos, sale 1 solo valor final).
        
    2. filter() — Seleccionar o filtrar elementos
    ---------------------------------------------
    Aplica una función que debe retornar un valor booleano (True o False) 
    a cada elemento. Conserva únicamente los elementos donde la función 
    devuelva True.

    ¿Cuándo usarla? 
    ---------------
    Cuando necesites descartar elementos que no cumplan con un criterio o 
    condición específica.
"""
numeros = [1, 2, 3, 4, 5, 6]

# Criterio: Conservar solo los pares (donde x % 2 == 0 sea True)
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)
# Salida: [2, 4, 6]  (Subconjunto del iterable original)
