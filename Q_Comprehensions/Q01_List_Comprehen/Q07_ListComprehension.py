""" El Creador de Iniciales
    Tienes una lista con nombres de personas y necesitas una lista que solo 
    tenga la primera letra de cada nombre en mayúscula.

    [ expresión_final for elemento in lista_original if condicion ]
"""

nombres = ["juan", "maria", "pedro", "ana"]
iniciales = [x[0].upper() for x in nombres]

print('Nombres originales', nombres)
print('Iniciales de los nombres', iniciales)

