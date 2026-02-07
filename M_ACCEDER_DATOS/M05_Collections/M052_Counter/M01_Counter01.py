""" COUNTER

    La Analogía: El Clasificador de Inventario
    ------------------------------------------
    Imagina que tienes una caja gigante llena de calcetines de muchos colores 
    mezclados. Quieres saber cuántos tienes de cada color.

    Sin Counter     Tendrías que sacar uno, anotar el color, buscar en una lista 
                    si ya anotaste ese color, sumarle uno...
    Con Counter     Es como si tuvieras un asistente mágico al que le pasas la 
                    caja y, en un segundo, te entrega una tablita que dice: 
                    "Rojos: 5, Azules: 3, Verdes: 1".
"""
from collections import Counter

frutas = ["manzana", "pera", "manzana", "naranja", "pera", "manzana"]

# Creamos el contador
conteo = Counter(frutas)

        # Resultado: Counter({'manzana': 3, 'pera': 2, 'naranja': 1})
print(conteo)
