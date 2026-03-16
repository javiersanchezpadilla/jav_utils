""" La anatomía de una f-string

    Existe un patron en los f-string dentro de las llaves, dos puntos (:) 
    se llama:
    
    Mini-lenguaje de especificación de formato de Python.
    -----------------------------------------------------
    La estructura completa es:

        {variable : [relleno][alineación][ancho][separador][.precisión][tipo]}

    Dato curioso: No necesitas aprenderte todos de memoria. Los más usados siempre 
    serán .2f (dinero/ciencias), , (contabilidad) y %d/%m/%Y (fechas).


    3. Fechas: El cronómetro (datetime)
    -----------------------------------

    Para desplegar formato en fechas se usan directivas. Aquí las más importantes:

        *) %d       Día del mes (01 a 31).
        *) %m       Mes en número (01 a 12).
        *) %Y       Año completo (2026).
        *) %H:%M    Horas y minutos.
        *) %A       Nombre del día (Lunes).
        *) %B       Nombre del mes (Febrero).
"""

from datetime import datetime
ahora = datetime.now()

print(f"{ahora:%d/%m/%Y}")          # 23/02/2026
print(f"{ahora:%I:%M %p}")          # 09:42 AM
print(f"{ahora:%A, %d de %B}")      # Monday, 23 de February
