""" ¿Para qué sirve esto en la vida real?

    El uso más común y útil es limpiar listas.
    Imagina que tienes una lista de correos electrónicos de clientes, pero 
    algunos se registraron dos veces por error:
"""

correos_sucios = ["ana@mail.com", "juan@mail.com", "ana@mail.com", "pedro@mail.com"]

# Convertimos a conjunto para borrar duplicados y luego volvemos a lista
correos_limpios = list(set(correos_sucios))

print(correos_limpios)
# Resultado: ['juan@mail.com', 'pedro@mail.com', 'ana@mail.com']
