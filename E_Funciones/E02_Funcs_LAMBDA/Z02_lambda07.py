""" Uniendo todo: Lambda + Map

    Para cerrar este tema, el último paso es aplicar esa herramienta que creaste 
    a una lista completa de una sola vez. En programación, esto es muy común cuando 
    quieres transformar una columna entera de datos.

    El Reto Final: Aplica esa misma lógica a la lista numeros usando map().

    Entrada: numeros = [1, 2, 3, 4, 5, 6]
    Misión: Si es par, multiplícalo por 10, si es impar, déjalo igual.

numeros = [1, 2, 3, 4, 5, 6]
# Tu código aquí usando list(map(lambda... , numeros))"""

numeros = [1, 2, 3, 4, 5, 6]
multiplicados = list(map(lambda numero: numero * 10 if numero % 2 == 0 else numero, numeros))

print('Lista de valores originales', numeros)
print('Lista multiplicada', multiplicados)
