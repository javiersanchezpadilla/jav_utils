""" LOS MAS COMUNES.

    no solo cuenta, sino que tiene funciones muy útiles para el día a día:

    1. Los más comunes (most_common). Si tienes una lista de mil elementos 
       y solo quieres saber cuáles son los 2 que más se repiten:
"""
from collections import Counter

frutas = ["manzana", "pera", "manzana", "naranja", "pera", "manzana"]

# Creamos el contador
conteo = Counter(frutas)

        # Resultado: Counter({'manzana': 3, 'pera': 2, 'naranja': 1})
print('El conteo es:', conteo)

        # Trae los 2 elementos que más aparecen
        # Resultado: [('manzana', 3), ('pera', 2)]
print('Los dos elementos mas repetidos son:', conteo.most_common(2))
