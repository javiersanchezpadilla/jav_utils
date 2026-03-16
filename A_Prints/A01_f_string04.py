""" La anatomía de una f-string

    Existe un patron en los f-string dentro de las llaves, dos puntos (:) 
    se llama:
    
    Mini-lenguaje de especificación de formato de Python.
    -----------------------------------------------------
    La estructura completa es:

        {variable : [relleno][alineación][ancho][separador][.precisión][tipo]}

    Dato curioso: No necesitas aprenderte todos de memoria. Los más usados siempre 
    serán .2f (dinero/ciencias), , (contabilidad) y %d/%m/%Y (fechas).


    4. Sistemas Numéricos: El código binario
    ----------------------------------------

    Si alguna vez necesitas convertir números a otras bases (como en informática 
    pura), es muy fácil:

        *) b    Binario.
        *) x    Hexadecimal.
        *) o    Octal.
"""
numero = 25
print(f"Binario: {numero:b}")  # 11001
print(f"Hex: {numero:x}")      # 19
