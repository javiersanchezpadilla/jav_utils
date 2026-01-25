""" Supongamos que solo quieres los números pares de una lista.

    [ expresión_final for elemento in lista_original if condicion ]
"""

edades = [12, 21, 34, 45, 18, 50]

edades_pares = [edad for edad in edades if edad % 2 == 0]

print(edades)
print(edades_pares)
