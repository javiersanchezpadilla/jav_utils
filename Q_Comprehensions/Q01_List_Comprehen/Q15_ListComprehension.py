""" Transformador Selectivo
    Multiplica por 100 los números positivos, pero deja los números negativos exactamente como están.

    Entrada: valores = [10, -5, 3, -1]
    Pista: La condición es if x > 0.

    [ valor_si_se_cumple if condicion else valor_si_no for elemento in lista ]
"""

valores = [10, -5, 3, -1]
multiplicados = [x if x < 0 else x*100 for x in valores]

print('Lista original', valores)
print('multiplica positivos', multiplicados)

