""" Pasar múltiples iterables

    Si le pasas más de un iterable, la función debe aceptar tantos argumentos 
    como iterables le envíes. map() procesará los elementos en parejas 
    (o grupos):
    
    Puntos clave a tomar en cuenta
    ------------------------------
    1)  Evaluación perezosa (Lazy Evaluation): map() no crea una lista 
        completa en memoria inmediatamente. Devuelve un objeto map (un 
        iterador). Si necesitas ver todos los elementos como una lista, 
        debes envolverlo con list(): list(map(...)).
    2)  Alternativa moderna (Comprensión de listas): En el Python moderno, 
        las comprensiones de listas suelen preferirse por ser más legibles 
        para la mayoría de los desarrolladores:

    >>> Con map(): list(map(lambda x: x * 2, numeros))
    >>> Con comprensión: [x * 2 for x in numeros]
"""
base = [2, 3, 4]
exponentes = [2, 3, 2]

# pow(x, y) calcula x elevado a y
potencias = list(map(pow, base, exponentes))

print(potencias)
# Salida: [4, 27, 16] (es decir: 2^2, 3^3, 4^2)