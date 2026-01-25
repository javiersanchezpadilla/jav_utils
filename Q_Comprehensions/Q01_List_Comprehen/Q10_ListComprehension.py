""" La Estructura con if-else
    A diferencia del filtro simple, cuando usamos else, la condición se pone al principio:

    [ valor_si_se_cumple if condicion else valor_si_no for elemento in lista ]

    Termómetro de Control
    Clasifica una lista de temperaturas. Si es mayor o igual a 30, pon la palabra "Calor", 
    de lo contrario, pon "Normal".

    Entrada: temps = [22, 35, 18, 40]
    Objetivo: ["Normal", "Calor", "Normal", "Calor"]
"""

temps = [22, 35, 18, 40]

clasificacion_temperaturas = ["Calor" if x >= 30 else "Normal" for x in temps]

print('Temperaturas originales', temps)
print('Clasificacion', clasificacion_temperaturas)


