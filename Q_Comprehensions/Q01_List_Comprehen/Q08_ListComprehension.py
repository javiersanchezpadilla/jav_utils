""" Buscador de Números Divisibles
    Utiliza la función range(1, 31) para generar una lista que solo contenga 
    los números del 1 al 30 que sean divisibles entre 3.

    [ expresión_final for elemento in lista_original if condicion ]
"""

lista_divisibles_tres = [x for x in range(1, 31) if x % 3 == 0]

print('Lista de valores entre 1 y 30 solo los divisibles entre tres')
print(lista_divisibles_tres)
