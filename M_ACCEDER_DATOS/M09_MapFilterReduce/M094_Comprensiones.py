""" Equivalencia con Comprensiones de Listas en Python Moderno

    En la práctica docente y profesional de Python, map() y filter() suelen 
    reemplazarse por comprensiones de listas (list comprehensions), ya que 
    resultan más legibles e idiómaticas:
"""
numeros = [1, 2, 3, 4, 5]

# Con map/filter tradicionales:
resultado_tradicional = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numeros)))

# Con comprensión de lista (más idiómático):
resultado_pythonico = [x * 2 for x in numeros if x % 2 == 0]

print(resultado_pythonico)  # Salida: [4, 8]
