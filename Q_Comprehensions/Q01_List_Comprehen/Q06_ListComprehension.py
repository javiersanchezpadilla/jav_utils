""" Filtro de Palabras Cortas
    Dada una lista de frutas, crea una nueva lista que solo contenga las 
    frutas que tengan más de 5 letras.

    [ expresión_final for elemento in lista_original if condicion ]
"""

frutas = ["pera", "manzana", "uva", "kiwi", "fresa", "pina"]
frutas_mas_de_cinco_letras = [fruta for fruta in frutas if len(fruta) > 5]

print('La lista de frutas original es', frutas)
print('Frutas que tienen mas de cinco letras', frutas_mas_de_cinco_letras)
