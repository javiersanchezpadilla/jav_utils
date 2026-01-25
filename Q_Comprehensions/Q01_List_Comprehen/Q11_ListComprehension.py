""" Calificador de Exámenes
    Tienes las notas de unos alumnos. Si la nota es 60 o más, el valor debe ser 
    "Aprobado", si es menor, debe ser "Reprobado".

    Entrada: notas = [85, 40, 62, 55]
    Objetivo: Generar la lista de estados.

    [ valor_si_se_cumple if condicion else valor_si_no for elemento in lista ]
"""

notas = [85, 40, 62, 55]
resultados = ["Aprobado" if x >= 60 else "Reprobado" for x in notas]

print('Notas originales', notas)
print('Clasificacion de las notas', resultados)
