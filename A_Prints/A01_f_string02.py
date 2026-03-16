""" La anatomía de una f-string

    Existe un patron en los f-string dentro de las llaves, dos puntos (:) 
    se llama:
    
    Mini-lenguaje de especificación de formato de Python.
    -----------------------------------------------------
    La estructura completa es:

        {variable : [relleno][alineación][ancho][separador][.precisión][tipo]}

    Dato curioso: No necesitas aprenderte todos de memoria. Los más usados siempre 
    serán .2f (dinero/ciencias), , (contabilidad) y %d/%m/%Y (fechas).


    2. Alineación y Relleno: El decorador de interiores
    ---------------------------------------------------

    A veces quieres que los datos se vean como una tabla perfecta en la consola.
    Usamos los símbolos <, >, y ^.

        *) <    Alinea a la izquierda (por defecto para texto).
        *) >    Alinea a la derecha (por defecto para números).
        *) ^    Centra el contenido.
"""

texto = "HOLA"
print(f"|{texto:<10}|")  # |HOLA      | (10 espacios total)
print(f"|{texto:>10}|")  # |      HOLA|
print(f"|{texto:^10}|")  # |   HOLA   |

# Puedes rellenar los espacios vacíos con un carácter:
print(f"{texto:=^20}")   # ========HOLA========
