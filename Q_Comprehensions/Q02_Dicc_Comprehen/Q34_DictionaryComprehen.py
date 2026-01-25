""" Filtrar un diccionario (Usando if)
    Imagina que tienes un inventario y solo quieres los productos que 
    tienen más de 0 existencias.

    inventario = {"Manzanas": 10, "Peras": 0, "Uvas": 5, "Mangos": 0}

    Recomendación: Usar .items() para poder extraer tanto la clave (prod) 
    como el valor (cant) al mismo tiempo.
"""

inventario = {"Manzanas": 10, "Peras": 0, "Uvas": 5, "Mangos": 0}

productos = {prod:cant for prod, cant in inventario.items() if cant > 0}

print('inventrio original', inventario)
print('Productos existentes:', productos)

