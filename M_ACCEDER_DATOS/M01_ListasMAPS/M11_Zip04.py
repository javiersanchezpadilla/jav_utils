""" ZIP() Con mas de dos listas

    ¿Y si tengo más de dos listas?
    zip no tiene límites. Puedes unir tantas listas como quieras, siempre y 
    cuando quieras formar grupos de esa misma cantidad.

    Ejemplo de una tienda: Imagina que quieres organizar tu inventario: 
    Producto, Precio y Cantidad.

    Lo que pasó aquí: Python tomó el primer elemento de cada una de las tres 
    listas y te los entregó en una sola pasada. Es como si unieras tres hileras 
    de un cierre.

"""

productos = ["Manzana", "Pan", "Leche"]
precios = [1.5, 2.0, 1.2]
cantidades = [10, 5, 20]

                         # *********************************   
for prod, precio, cant in zip(productos, precios, cantidades):
    total_producto = precio * cant
    print(f"Hay {cant} unidades de {prod}. Valor total: ${total_producto}")

