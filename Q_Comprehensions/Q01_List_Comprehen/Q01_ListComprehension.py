""" LIST COMPREHENSION.

    La Estructura.

    La fórmula mágica para leer estas líneas es:

            [ lo que quiero obtener | el ciclo for | la condición (opcional) ]

    Lo que quiero obtener       Es la operación o el valor que se guardará en 
                                la nueva lista (ej. n * n).
    El ciclo for                Indica de dónde sacamos los datos (ej. for n in numeros).
    La condición                Un filtro para decidir qué elementos entran y cuáles 
                                no (ej. if n > 2).

"""

valores = [12, None, 100, None, None, 1, 2, 3, None]

lista_sin_nones = [valor for valor in valores if valor != None]
lista_none_por_cero = [valor if valor != None else 0 for valor in valores]

print(valores)
print(lista_sin_nones)
print(lista_none_por_cero)

