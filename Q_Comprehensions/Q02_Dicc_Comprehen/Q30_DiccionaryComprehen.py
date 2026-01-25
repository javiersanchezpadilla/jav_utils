""" Tienes una lista de productos y sus precios. 

    Crea un diccionario donde la clave sea el nombre del producto y 
    el valor sea el precio, pero sumándole $5 de costo de envío a cada uno.

        productos = [("Laptop", 800), ("Mouse", 20), ("Teclado", 50)]

    Pista: Como es una lista de tuplas, tu ciclo debe empezar así: for nombre, precio in productos
"""

productos = [("Laptop", 800), ("Mouse", 20), ("Teclado", 50)]

mi_diccionario = {nombre: precio + 5 for nombre, precio in productos}

print('La lista de los productos:', productos)
print('El diccionario creado:', mi_diccionario)
