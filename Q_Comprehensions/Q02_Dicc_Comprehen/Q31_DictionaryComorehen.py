""" Un paso más allá: El "If-Else" en Diccionarios
Al igual que en las listas, también puedes tomar decisiones sobre los valores.

Reto Final (Bonus): Imagina que quieres un diccionario que clasifique el stock. 
Si hay más de 5 unidades pon "Suficiente", si hay menos pon "Reponer".

Entrada: stock = {"manzanas": 2, "peras": 8}

Objetivo: {"manzanas": "Reponer", "peras": "Suficiente"}"""

stock = {"manzanas": 2, "peras": 8}

clasificacion_stock = {fruta: "Suficiente" if cantidad > 5 else "Reponer" for fruta, cantidad in stock.items()}

print("Stock original:", stock)
print("Clasificación del stock:", clasificacion_stock)
