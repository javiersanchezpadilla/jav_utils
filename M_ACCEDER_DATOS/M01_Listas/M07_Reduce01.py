""" REDUCE 

    Combina elementos.
    Acumula resultados"""

from functools import reduce

numeros = [1, 2, 3, 4]
total = reduce(lambda x, y : x + y, numeros)

print(total)    # 10
