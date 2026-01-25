""" Filtro de Inventario (Nivel Medio)

    Tienes un diccionario con frutas y sus cantidades. 
    Crea un nuevo diccionario que solo contenga las frutas que tienen 5 o más unidades.

    stock = {"manzanas": 2, "peras": 8, "naranjas": 4, "platanos": 12}

    Pista: Usa stock.items() para obtener fruta, cantidad.
"""

stock = {"manzanas": 2, "peras": 8, "naranjas": 4, "platanos": 12}

nuevo_dicionario = {fruta: unidades for fruta, unidades in stock.items() if unidades >= 5}

print('Strock original:', stock)
print('Nuevo diccionario:', nuevo_dicionario)
