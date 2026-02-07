""" Intercambio de Variables.

    En otros lenguajes, para intercambiar el valor de dos variables necesitas 
    una "variable temporal" (como una tercera mano para sostener un vaso 
    mientras cambias el otro). En Python, el unpacking lo hace instantáneo:

    Resumen sencillo:
    -----------------
    Unpacking       Es sacar elementos de una lista/tupla y darles su propio 
                    nombre (variable).
    Asterisco *     Sirve para agrupar "todo lo que sobre" en una nueva lista.
    Uso principal   Hace que el código sea mucho más corto y fácil de leer, 
                    evitando usar índices como lista[0], lista[1], etc.
"""
a = "Fuego"
b = "Agua"

                # Intercambio directo
a, b = b, a

                # Resultado: a es Agua y b es Fuego
print(f"a es {a} y b es {b}")
