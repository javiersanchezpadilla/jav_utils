""" El Convertidor de Precios 
    Tienes una lista de precios en pesos y quieres crear una nueva lista que 
    tenga esos mismos precios pero con un descuento del 10% (es decir, multiplicarlos por 0.9).
    Objetivo: Obtener los nuevos precios en una sola línea.

    [ expresión_final for elemento in lista_original if condicion ]
"""

precios = [100, 250, 50, 400]

lista_con_descuento = [x * 0.9 for x in precios]

print('Lista de precios', precios)
print('Lista con descuento', lista_con_descuento)
