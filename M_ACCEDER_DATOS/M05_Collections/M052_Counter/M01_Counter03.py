""" Operaciones matemáticas entre contadores.

    Puedes sumar o restar contadores como si fueran números. 
    Imagina que tienes un inventario hoy y vendes algunos productos:

    ¿Cuándo usarlo en la vida real?
    -------------------------------
    Analizar textos         Para saber qué palabras usa más un autor.
    Sistemas de votación    Para contar votos rápidamente.
    E-commerce              Para ver qué productos son los "Best Sellers".

    Resumen rápido:
    ---------------
    Counter         Es un diccionario especializado en contar.
    Entrada         Le puedes pasar listas, tuplas o incluso texto.
"""
from collections import Counter

inventario = Counter(manzanas=10, peras=5)
ventas = Counter(manzanas=3, peras=2)

            # ¿Qué nos queda? ¡Simplemente restamos!
stock_final = inventario - ventas

            # Resultado: Counter({'manzanas': 7, 'peras': 3})
print(stock_final)
