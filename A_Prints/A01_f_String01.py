""" La anatomía de una f-string

    Existe un patron en los f-string dentro de las llaves, dos puntos (:) 
    se llama:
    
    Mini-lenguaje de especificación de formato de Python.
    -----------------------------------------------------

    La estructura completa es:

        {variable : [relleno][alineación][ancho][separador][.precisión][tipo]}

    Dato curioso: No necesitas aprenderte todos de memoria. Los más usados siempre 
    serán .2f (dinero/ciencias), , (contabilidad) y %d/%m/%Y (fechas).

    Imagina que las f-strings son como una invitación: lo que va antes de los
    dos puntos es "quién" viene a la fiesta (la variable), y lo que va después
    es "cómo" debe vestirse (el formato).

    1. Números: El traje de gala
    ----------------------------
    Además de los decimales que ya conoces (.2f), puedes controlar miles, signos 
    y alineación.

        *) Separador de miles: Usa una coma , o un guion bajo _.
        *) Signo siempre visible: Usa + para mostrar si un número es positivo o negativo.
        *) Porcentajes: La f se cambia por % y Python multiplica por 100 automáticamente.
"""
valor = 1500.5
print(f"{valor:,.2f}")  # 1,500.50 (Miles y 2 decimales)
print(f"{valor:+}")     # +1500.5  (Forzar el signo)
print(f"{valor:+,}")    # +1,500.5  (Forzar el signo y separador de miles)

avance = 0.756
print(f"{avance:.1%}")  # 75.6%    (Formato porcentaje)

