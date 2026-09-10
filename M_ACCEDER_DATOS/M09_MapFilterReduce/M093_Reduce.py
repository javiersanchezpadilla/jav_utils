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
        
    3. reduce() — Acumular en un único valor
    ----------------------------------------
    A diferencia de map y filter (que están integradas de forma nativa), 
    reduce() se debe importar desde el módulo functools.
    Aplica una función de dos argumentos de forma acumulativa a los elementos 
    de la secuencia, de izquierda a derecha, combinándolos progresivamente 
    hasta reducirlos a un único valor.

    ¿Cuándo usarla? 
    Cuando necesites calcular un total acumulado, un producto, encontrar un 
    valor extremo (máximo/mínimo) o combinar una lista en una sola estructura.
"""
from functools import reduce

numeros = [1, 2, 3, 4]

# Suma acumulada: (((1 + 2) + 3) + 4)
suma_total = reduce(lambda acumulador, elemento: acumulador + elemento, numeros)

print(suma_total)
# Salida: 10  (Un solo valor como resultado)
