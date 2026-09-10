""" Con funciones lambda (Anonimas)

    Si la transformación es sencilla y solo la usarás una vez, se suele 
    combinar map() con una función lambda:
"""
precios = [100, 200, 300]

# Duplicar cada precio
precios_dobles = list(map(lambda x: x * 2, precios))

print(precios_dobles)
# Salida: [200, 400, 600]
