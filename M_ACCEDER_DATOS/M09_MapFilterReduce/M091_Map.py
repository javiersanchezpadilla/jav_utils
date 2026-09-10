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
        
    1. map() — Transformar elementos
    ---------------------------------
    Aplica una función a cada uno de los elementos de un iterable para 
    generar una nueva secuencia con la misma cantidad de items.¿Cuándo 
    usarla? Cuando necesites convertir, modificar o extraer datos de cada 
    elemento de una lista de forma individual.

"""
numeros = [1, 2, 3, 4, 5]

# Transformación: Elevar al cuadrado
cuadrados = list(map(lambda x: x**2, numeros))

print(cuadrados)
# Salida: [1, 4, 9, 16, 25]  (Misma cantidad de elementos)
