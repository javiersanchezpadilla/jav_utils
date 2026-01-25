""" El Etiquetador de Precios
    Aplica una etiqueta a los productos. Si el precio es mayor a 500, 
    etiquétalo como "Caro", si no, etiquétalo como "Barato".

    Entrada: precios = [100, 800, 250, 1200]
    Objetivo: Obtener la lista de etiquetas.

    [ valor_si_se_cumple if condicion else valor_si_no for elemento in lista ]
"""

precios = [100, 800, 250, 1200]
precios_etiquetados = ["Caro" if x > 500 else "Barato" for x in precios]

print('Lista de precios original', precios)
print('Clasificación de los precios', precios_etiquetados)

